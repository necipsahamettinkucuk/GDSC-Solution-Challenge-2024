
import cv2
class Cam:

    def __init__(self):

        self.rtsp_url = "rtsp://admin:Grunding1234@192.168.1.100:554/Streaming/Channels/2"
        #ip camera information

    def read_with_ai(self, ai):

        
        video_capture = cv2.VideoCapture(self.rtsp_url, cv2.CAP_FFMPEG)
        video_capture.set(cv2.CAP_PROP_BUFFERSIZE, 0)

        if not video_capture.isOpened():
            print("açılmadı.")
            exit()

        while True:
            ret, frame = video_capture.read()

            
            ai.model_tespit(frame)

            if not ret:
                print("The stream has ended.")
                break

            
            cv2.imshow('IP KAMERA', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        
        video_capture.release()
        cv2.destroyAllWindows()
