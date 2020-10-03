# Mobiliaire
A lightweight property inventory helper

> mobiliaire (n.): Middle French form of "mobiliary"; pertaining to furniture or movable property

## Still in development (v0.\*). Main branch is generally stable. 1.0 coming soon to a "stable" branch near you.

*built for/on Django 3.1*

This app is for assisting SCA branches in managing both annual inventories and pack-in/pack-out at events. It is designed to be installed on a portable machine - to be taken to events and serve up web pages with inventory information without needing access to the Internet. A [$35 Raspberry Pi](https://www.raspberrypi.org/products/) fits the bill nicely here, but take my advice and spend the extra $10 for a [case](https://www.raspberrypi.org/products/raspberry-pi-4-case/) if you go that route. A tablet with Termux or a similar application may work as well.

See it in action at https://cordelya.pythonanywhere.com (note: this will be whatever's in the main branch - changes in dev branches won't be available)

Want to try it out? 

````
$ git clone https://github.com/Cordelya/mobiliaire.git
````
[See a more detailed procedure.](https://github.com/Cordelya/mobiliaire/wiki/getStarted)

Inventory Items are grouped into Boxes (which can be literal or virtual boxes), which are then further grouped into Warehouses. In this context, a warehouse is a geographic location where a box or boxes are stored. A branch cargo trailer full of items is a Warehouse. Examples of virtual boxes include the "loose in the trailer" box, the "driver-side cargo rack" box, or the "gold-key-closet" box. 

Key: (N) = not yet implemented

* Tracks whether items are consumable or not
* Tracks the replacement value of each item. Front-end displays total aggregate value on index, and sub-values on Warehouse and Box detail pages.
* Set keywords to make search results filter-able. Add as many keywords as applicable. Suggested keywords include "Category: <category>" for categories like "kitchen" "archery" "heraldic" etc; "Color: <color>" to classify items by their main color(s); "Material: <material>" to classify by material (glass, metal, plastic, etc)
  * Keywords show on item detail page
  * Keyword detail pages list all items
* Move items from one box to another by updating the current box's end date and creating a new items_in_boxes record for the new box, leaving the end date blank. Item's box history will be preserved. Front end shows only current location.
* Reports: 
  * PDF/Excel/CSV/Print export of any data on reports pages. Each table has its own set of export buttons, allowing you to build a custom report. You can filter tables before exporting and only export the filtered rows. You can sort columns before exporting and the sort order will be reflected in the result.
     * Page /reports/full/ has all data presented, requiring the report-generator to click only four buttons (warehouse list, boxes by ID, boxes by name, and items). 
     * At this time, print or pdf reports with each box separated can be done via the reports/wh/ page but it requires clicking each box's export button. One-click button triggering is deferred until after version 1.0 is released.
  * CSV import is implemented but it is up to the site admin to set up the import config for each csv file to be imported. This means you can, in theory, config the importer to import your entire inventory spreadsheet, no matter what condition it is in. For the rest of us, start with staff, warehouses, and keywords, then do boxes, then items and attach your items to the appropriate box and keywords.
  * export database as database-friendly backup file (available on command-line)
  * (N) consumable items, per box, for printing to allow event staff or annual inventory staff to verify quantities remaining and make notes.
     * A stopgap is available on the box report page - type "True" in the search box on each table and click "PDF" and you have a list. 
 * Pack-in/out friendly search: when an item is needed or arrives for packing, begin search with general item description (ie "ladle"), filter items by keyword (Category: Kitchen, Material: Metal, etc.) until matching item is identified (verify visually via inline photo) and place item in indicated box. Can go very quickly if a person familiar with the system is staffing the search terminal. For best results, limit search query to a single word (complex search planned for after version 1.0 is released)
     * Items report table (/reports/items/) is also fully searchable, but does not display pictures and does not include keywords. Would need to click through to each search result to verify. Displaying item image files via Bootstrap modal is planned for after 1.0 is released.
 * Warehouse detail page shows photo associated with warehouse, if set. This could be an image of an individual's or officer's armory, or a photo of the physical warehouse.
     * Defaults to "warehouse.png" to facilitate using a placeholder file.
 * Box listing on warehouse detail, box list, and box detail includes photo of box, if set. 
     * Defaults to "box.png" to facilitate using a placeholder file.
 * Item listing on box detail, item list, and item detail shows item photo, if set. Set photo by saving image file to /static/inv/img and recording the image's filename in the item's record. Recommended image file naming convention: by item ID, item name, or combo. Image name field and image name (including extension, but excluding path) must match exactly. Run python manage.py collectstatic after adding any files to the static/ folder tree. 
     * If image is not set, helper text asks viewer to snap a photo of the item and email it to the inventory management contact with the item's id number in the subject line (item id number is displayed). Adding photos via webcam control is planned for a release after 1.0.

This app is built on a well-established and well-documented framework. If you're not sure how to do something, try checking the Django documentation pages first.
