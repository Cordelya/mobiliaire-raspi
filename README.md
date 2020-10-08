# Mobiliaire-raspi
A Raspberry Pi flavored lightweight property inventory helper

> mobiliaire (n.): Middle French form of "mobiliary"; pertaining to furniture or movable property

Please see the main [Mobiliaire](https://github.com/Cordelya/mobiliaire) for information about the application. This page only details the specific features available in this fork.

## PiCamera Support

This fork will allow you to use a Raspberry Pi camera to collect images on the fly. Each image will be stored in 'mobiliaire/static/inv/img/new/' with a unique filename that includes a reference to the item, box, or warehouse page we used to initiate the photograph.

Raspberry Pi Cameras are available for purchase separately from the main Raspberry Pi board, or you may be able to find it as part of a bundle. There are several versions. You likely want the "Camera Module v2" version.

You will also need to manufacture a way to mount the camera board so it can be pointed at your photo booth or backdrop. While this overall is beyond the scope of this repository, you may be interested to know that camera cases with LEGO brick attachment points are available for purchase from some suppliers.

Before you can run this fork on a Raspberry Pi, you should view the [Raspi Camera Startup Guide](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera) which will walk you through installing your camera, enabling it, and testing that it is working properly. You should test that the camera is working properly every time you plug it in to your Raspberry Pi board (remember - the blue tab faces toward the Ethernet/USB ports on most models, and always loosen the cable receiver clip before inserting or removing ribbon cables)
After you have done initial camera setup, you can test your camera on the command line by running:
````
$ raspistill -o testshot.jpg
````
If the camera is properly attached, you will see the camera preview for a few seconds, then it will disappear, and a photo named "testshot.jpg" should appear in the folder where you ran the test. You can remove the test photo once you have confirmed that it is there. 

Follow the install procedure in [Mobiliaire Wiki: Getting Started](https://github.com/Cordelya/mobiliaire/wiki/getStarted), but instead of git cloning [http://github.com/Cordelya/mobiliaire.git] you will git clone [http://github.com/Cordelya/mobiliaire-raspi.git]

