
# polygon falan ai da dursun

import ultralytics
import cv2
import supervision as sv
import numpy as np

class Model:

    def __init__(self, path):

        self.model = self.model_yukle(path)
        #initiate polygon zone
        self.polygon = np.array([
            [0, 0],
            [1, 0],
            [1, 1],
            [0, 1]
        ])  # 30

    def model_yukle(self, path):

        return ultralytics.YOLO(path)

    def model_al(self):

        return self.model

    def model_tespit(self, frame):

        zone = sv.PolygonZone(polygon=self.polygon, frame_resolution_wh=(640, 480))

        # initiate annotators
        box_annotator = sv.BoxAnnotator(thickness=1, text_thickness=2, text_scale=2)
        zone_annotator = sv.PolygonZoneAnnotator(zone=zone, color=sv.Color.white(), thickness=2, text_thickness=2, text_scale=1)

        # detect
        results = self.model(frame, imgsz=640)[0]
        detections = sv.Detections.from_ultralytics(results)
        alandakiler = zone.trigger(detections=detections)
        sayi = len(alandakiler[alandakiler == True])


        # annotate
        box_annotator = sv.BoxAnnotator(thickness=1, text_thickness=1, text_scale=1)
        labels = [f"{self.model.names[class_id]} {confidence:0.2f} " for _, _, confidence, class_id, _ in detections]
        frame = box_annotator.annotate(scene=frame, detections=detections[alandakiler], labels=labels, skip_label=None)
        frame = zone_annotator.annotate(scene=frame)    # Sadece bu kısmı yorum satına alarakta yapabiliriz

        # printing the number of visible objects in the upper left corner
        cv2.putText(frame, str(sayi), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)




