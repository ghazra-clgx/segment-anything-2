# Works, Need to test with custom dataset

import pixellib
from pixellib.torchbackend.instance import instanceSegmentation

ins = instanceSegmentation()
ins.load_model("C:\\Users\\ghazra\\Downloads\\pointrend_resnet50.pkl")
ins.process_video("C:\\Users\\ghazra\\Desktop\\CoreLogic\\MICA.WebApps.LLMServer\\segment-anything-2\\video\\floor_dmg.mp4", show_bboxes=True, frames_per_second=3, output_video_name="C:\\Users\\ghazra\\Downloads\\floor_dmg_seg.mp4")


# target_classes = ins.select_target_classes(person = True, bicycle =True)
# ins.process_video("sample_video.mp4", show_bboxes=True, segment_target_classes = target_classes,
# frames_per_second=5, output_video_name="output_video.mp4")