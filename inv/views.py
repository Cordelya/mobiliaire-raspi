from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Warehouse, Boxes, Items, Staff, Items_in_boxes, Keywords, Keywords_in_items, Inventory
from django.db.models import Count, Sum, Q, F, DecimalField, FloatField, IntegerField, ExpressionWrapper
from django.db.models.functions import Lower
from decimal import Decimal
from picamera import PiCamera
from time import sleep
from datetime import datetime

def index(request):
    item_count = Items.objects.all().annotate(Count("item_id"))
    box_count = Boxes.objects.all().annotate(Count("box_id"))
    warehouse_count = Warehouse.objects.all().annotate(Count("warehouse_id"))
    val = Items.objects.all().annotate(ival=Sum(F('item_value')*F('item_qty'), output_field=FloatField())).aggregate(val=Sum("ival"))
    return render(request, 'inv/index.html', {'item_count' : item_count, 'box_count' : box_count, 'warehouse_count' : warehouse_count, 'val' : val })

def dash(request):
    return render(request, 'inv/dash.html', {})

def search(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        if search == None:
            return render(request, 'inv/search.html')
        else:
            result = Items.objects.filter(item_name__icontains=search).prefetch_related().annotate(box=F('itm_id__box_id__box_name')).annotate(boxid=F('itm_id__box_id')).annotate(wh=F('itm_id__box_id__warehouse__warehouse_name')).annotate(whid=F('itm_id__box_id__warehouse')).annotate(totval=Sum(F('item_value')*F('item_qty'), output_field=FloatField())).annotate(sort_name=Lower('item_name')).order_by('sort_name')
            kw_result = Keywords.objects.filter(keyword__icontains=search)
            box_result = Boxes.objects.filter(box_name__icontains=search)
            wh_result = Warehouse.objects.filter(warehouse_name__icontains=search)
            kw = Keywords.objects.only('keyword').order_by('keyword')
            return render(request, 'inv/search.html', {'result' : result, 'kw_result' : kw_result, 'kw' : kw, 'box_result' : box_result, 'wh_result' : wh_result})
    else:
        return render(request, 'inv/search.html',)

def reports(request):
    return render(request, 'inv/reports.html')

def report_itm(request, item_sort=None):
    items = Items.objects.all().prefetch_related().annotate(box=F('itm_id__box_id__box_name')).annotate(wh=F('itm_id__box_id__warehouse__warehouse_name')).annotate(totval=Sum(F('item_value')*F('item_qty'), output_field=FloatField())).annotate(kw=F("item_id"))
    kw = Keywords_in_items.objects.all()
    for k in kw:
        k.kw=k.keyword_id.replace(': ', '-')
    return render(request, 'inv/rpt_items.html', {'items' : items, 'kw' : kw})

def report_box(request, box=None):
    if box:
        boxes = Boxes.objects.filter(box_id=box)
    else:
        boxes = Boxes.objects.all()
    items = Items.objects.all().prefetch_related().annotate(boxid=F('itm_id__box_id')).annotate(totval=Sum(F('item_value')*F('item_qty'), output_field=FloatField())).annotate(sort_name=Lower('item_name')).order_by('sort_name')
    return render(request, 'inv/rpt_boxes.html', {'items' : items, 'boxes' : boxes})

def report_wh(request, whid=None):
    # warehouse report for a single warehouse
    if whid:
        wh = Warehouse.objects.filter(warehouse_id=whid)
    else: wh = Warehouse.objects.all()
    box = Boxes.objects.all().prefetch_related().annotate(whid=F('warehouse__warehouse_id'))
    items =  items = Items.objects.all().prefetch_related().annotate(boxid=F('itm_id__box_id')).annotate(totval=Sum(F('item_value')*F('item_qty'), output_field=FloatField())).annotate(sort_name=Lower('item_name')).order_by('sort_name')

    return render(request, 'inv/rpt_wh.html', {'items' : items, 'wh' : wh, 'box' : box})

def report_full(request):
    # full all-in-one inventory report for exporting via dataTables
    wh = Warehouse.objects.all().prefetch_related().annotate(box_count=Count('bx_wh__box_id'))
    box = Boxes.objects.all().prefetch_related().annotate(whid=F('warehouse__warehouse_id'))
    box_alpha = Boxes.objects.all().prefetch_related().annotate(whid=F('warehouse__warehouse_id')).annotate(sort_name=Lower('box_name')).order_by('sort_name')
    items =  items = Items.objects.all().prefetch_related().annotate(boxid=F('itm_id__box_id')).annotate(totval=Sum(F('item_value')*F('item_qty'), output_field=FloatField())).annotate(sort_name=Lower('item_name')).order_by('sort_name')

    return render(request, 'inv/rpt_full.html', {'items' : items, 'wh' : wh, 'box' : box, 'box_alpha': box_alpha})

def items(request):
    items = Items.objects.all().prefetch_related().annotate(box=F('itm_id__box_id__box_name')).annotate(boxid=F('itm_id__box_id')).annotate(wh=F('itm_id__box_id__warehouse__warehouse_name')).annotate(whid=F('itm_id__box_id__warehouse')).annotate(totval=Sum(F('item_value')*F('item_qty'), output_field=FloatField())).annotate(sort_name=Lower('item_name')).order_by('sort_name')
    kw = Keywords.objects.only('keyword').order_by('keyword')
    return render(request, 'inv/items.html', {'items' : items, 'kw' : kw})

def item(request, itemid):
    item = Items.objects.filter(item_id=itemid).annotate(totval=Sum(F('item_value')*F('item_qty'), output_field=FloatField())).get(item_id=itemid)
    box = Items_in_boxes.objects.filter(item_id=itemid).filter(date_to__isnull=True).annotate(name=F('box_id__box_name')).annotate(bx_id=F('box_id')).get(item_id=itemid)
    wh = Boxes.objects.filter(box_id=box.bx_id).annotate(name=F('warehouse__warehouse_name')).get(box_id=box.bx_id)
    kw = Keywords_in_items.objects.filter(item_id=itemid)
    return render(request, 'inv/item.html', {'item' : item , 'box' : box, 'wh' : wh, 'kw' : kw})

def boxes(request):
    boxes = Boxes.objects.all().annotate(num_items=Count('bx_id__item_id', filter=Q(bx_id__date_to__isnull=True)))
    return render(request, 'inv/boxes.html', {'boxes' : boxes })

def box(request, boxid):
    box = Boxes.objects.prefetch_related('warehouse').get(box_id=boxid)
    items = Items_in_boxes.objects.prefetch_related().filter(date_to__isnull=True).filter(box_id=boxid).annotate(item_img=F('item_id__item_img')).annotate(totval=Sum(F('item_id__item_value')*F('item_id__item_qty'), output_field=FloatField()))
    items.item_totals = Items_in_boxes.objects.filter(date_to__isnull=True).filter(box_id=boxid).aggregate(icount=Count('item_id'), val=Sum('item_id__item_value'))
    return render(request, 'inv/box.html', {'box' : box, 'items': items})

def warehouses(request):
    wh = Warehouse.objects.all().annotate(num_boxes=Count('bx_wh'))
    return render(request, 'inv/warehouses.html', {'wh' : wh})

def warehouse(request, whid):
    wh = Warehouse.objects.get(warehouse_id=whid)
    boxes = Boxes.objects.filter(warehouse_id=whid).annotate(num_items=Count('bx_id',
        filter=Q(bx_id__date_to__isnull=True))).annotate(val=Sum("bx_id__item_id__item_value",
            filter=Q(bx_id__date_to__isnull=True)))
    return render(request, 'inv/warehouse.html', {'wh' : wh, 'boxes' : boxes})

def consumables(request):
    consumables = Items.objects.filter(item_consumable=True).annotate(restock=ExpressionWrapper(F('item_qty') * ((100.0 - F('item_remaining'))/100.0), output_field=FloatField()))
    return render(request, 'inv/consumables.html', {'consumables' : consumables})

def inventories(request):
    return HttpResponse("Hello, world. You're at the Inventories Summary.")

def inventory(request, invid):
    return HttpResponse("Hello, world. You're looking at an individual inventory summary.")

def keywords(request, kw_slug=None):
    if kw_slug:
        keyword = Keywords.objects.get(keyword_slug=kw_slug)
        kw = Keywords_in_items.objects.prefetch_related().filter(keyword__keyword_slug=kw_slug)
        items = Items.objects.prefetch_related().filter(kw_itm__keyword__keyword_slug=kw_slug).annotate(box=F('itm_id__box_id__box_name')).annotate(boxid=F('itm_id__box_id')).annotate(wh=F('itm_id__box_id__warehouse__warehouse_name')).annotate(whid=F('itm_id__box_id__warehouse')).annotate(totval=Sum(F('item_value')*F('item_qty'), output_field=FloatField())).annotate(sort_name=Lower('item_name')).order_by('sort_name')
        return render(request, 'inv/keywords.html', {'keyword' : keyword, 'kw' : kw , 'items' : items})
    else:
        kw = Keywords.objects.all().prefetch_related().annotate(tot=Count('kw_kw__item_id'))
        return render(request, 'inv/keywords.html', {'kw' : kw})


def cameraCapture(request, fileName=None, fname=None):
    if fname:
        return render(request, 'inv/photo.html', {'fileName' : fileName, 'fname' : fname})
    elif fileName:
        date_time = datetime.now()
        fname = fileName + '_' + str(datetime.now()) + '.jpg'
        fname = str(fname)
        camera = PiCamera()
        camera.start_preview()
        sleep(5)
        camera.capture('/home/pi/Apps/mobiliaire/static/inv/img/new/%s' % fname)
        camera.stop_preview()
        camera.close()
        return redirect('/capture/%s/%s/' % (fileName, fname))
