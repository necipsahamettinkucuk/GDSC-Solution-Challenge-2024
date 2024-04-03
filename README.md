# GDSC-Solution-Challenge-2024
FOREST FIRE DETECTION

In order to operate this system, it works by receiving live video from the ip camera on a UAV. I have made some arrangements for you to run this system, so you will be able to run it even if you do not have a UAV. The 3050ti video card works on a laptop.<br>
<b>How will you make it work:<br></b>
Ask an IT person in the company for the "IP, username, password" information of an IP camera that sees people. Write this information on line 7 in the Camera class. <br>"self.rtsp_url = "rtsp://<b>username:password@camera IP</b>:554/Streaming/Channels/2"".<br><br>![image](https://github.com/necipsahamettinkucuk/GDSC-Solution-Challenge-2024/assets/121046682/04e1c67b-cb45-4ccb-9921-7b2324e260cb)
<br><br>
Then replace "ai = AI.Model("best.pt")" <b>best.pt</b> with <b>yolov8s.pt</b> in line 18 of main.<br>![image](https://github.com/necipsahamettinkucuk/GDSC-Solution-Challenge-2024/assets/121046682/14faaefb-343b-4556-95b2-6f725c2c192c) <br>

After these edits, run the main.py file. After this is done, you will see the number of objects in the place where the IP camera sees and you will see it.<br><br>
If you don't have a UAV, you can connect to any IP camera. If you train the data set I created in Colab and use that weight, you can detect fire. Or you can directly download the yolov8s weight and detect objects such as people, tables, books with the yolo weight trained with the COCO data set.

