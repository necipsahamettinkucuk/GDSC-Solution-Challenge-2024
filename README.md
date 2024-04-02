# GDSC-Solution-Challenge-2024
FOREST FIRE DETECTION

Bu sistemi çalıştırmak için bir tane İHA'ya bağlı ve bu İHA üstüne bulunun bir IP kameraya ihtiyacınız bulunmaktadır. Bu sistemi çalıştırmanız için size göre bazı düzenlemeler gerçekleştirdim.
Siz nasıl çalıştıracaksınız:
Firmadaki bir IT çalışanından insanları gören bir IP kamera "IP, usernamei, password" isteyin. Bu bilgileri Camera class'ının içindeki 7 satıra bulunan <i>"self.rtsp_url = "rtsp://<b>username:password@camera IP<b>:554/Streaming/Channels/2""<i>.
Ardından main'de 18. satırda bulunan "ai = AI.Model("best.pt")" <b>best.pt<b> yerine <b>yolov8s.pt<b> yazınız.
