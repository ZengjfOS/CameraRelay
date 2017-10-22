# Camera Relay

在树莓派上安装USB Camera，通过GPIO口控制设备电源，在电源上点一定时间后，对设备进行拍照。

**Ctrl+c**停止程序运行。

## 参考文档：
* [Getting Webcam Images with Python and OpenCV 2 (For Real This Time)](https://codeplasma.com/2012/12/03/getting-webcam-images-with-python-and-opencv-2-for-real-this-time/)
* [Python time to String](https://wangheng.org/html/python_datetime.html)
* [Python的命令行参数解析](http://noahsnail.com/2017/09/13/2017-9-13-Python%E7%9A%84%E5%91%BD%E4%BB%A4%E8%A1%8C%E5%8F%82%E6%95%B0%E8%A7%A3%E6%9E%90/)
* [RPi 2B GPIO 测试](http://www.cnblogs.com/zengjfgit/p/5215194.html)
* [RPi 2B python opencv camera demo example](http://www.cnblogs.com/zengjfgit/p/5223747.html)

## USAGE

### Help

```
usage: CameraRelay.py [-h] -on ON -off OFF -cap CAP

Camera Control Relay.

optional arguments:
  -h, --help  show this help message and exit
  -on ON      Power On Duty(s)
  -off OFF    Power Off Duty(s)
  -cap CAP    Camera Capture Image Delay After Power On(s)

Example: ./CameraRelay.py -on 4 -off 2 -cap 1
```

### Example

```
./CameraRelay.py -on 4 -off 2 -cap 1 
```

* Power On 4(s)
* Power Off 2(s)
* Capture a image after Power On 4(s)

### CMD Output Example

```
root@raspberrypi:/home/pi/CameraRelay# ./CameraRelay.py -on 4 -off 2 -cap 1
Namespace(cap='1', off='2', on='4')
 powerOnTime: 4.0.
 powerOffTime: 2.0.
 cameraCaptureDelay: 1.0.

start power off: 20171022065732
over power off and start power on: 20171022065734
capture a image: 20171022065735
over power on: 20171022065738
Capture image count: 1
start power off: 20171022065738
over power off and start power on: 20171022065740
capture a image: 20171022065741
over power on: 20171022065744
Capture image count: 2
start power off: 20171022065744
over power off and start power on: 20171022065746
capture a image: 20171022065747
over power on: 20171022065750
Capture image count: 3
```
