# GDSC-Solution-Challenge-2024
FOREST FIRE DETECTION

Bu sistemi çalıştırmak için bir tane İHA'ya bağlı ve bu İHA üstüne bulunun bir IP kameraya ihtiyacınız bulunmaktadır. Bu sistemi çalıştırmanız için size göre bazı düzenlemeler gerçekleştirdim.<br>
<b>Siz nasıl çalıştıracaksınız:<br></b>
Firmadaki bir IT çalışanından insanları gören bir IP kamera "IP, username, password" bilgilerini isteyin. Bu bilgileri Camera class'ının içindeki 7. satıra bulunan: <br>"self.rtsp_url = "rtsp://<b>username:password@camera IP</b>:554/Streaming/Channels/2"".<br><br>![image](https://github.com/necipsahamettinkucuk/GDSC-Solution-Challenge-2024/assets/121046682/04e1c67b-cb45-4ccb-9921-7b2324e260cb)
<br><br>
Ardından main'de 18. satırda bulunan "ai = AI.Model("best.pt")" <b>best.pt</b> yerine <b>yolov8s.pt</b> yazınız.
