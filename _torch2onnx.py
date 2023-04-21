import torch
from models.yolo import Model
import sys
# sys.path.append('../')

model = Model(cfg='./models/yolov5s.yaml')
model.load_state_dict(torch.load('./weights/yolov5s.pt')['model'].state_dict())

x = torch.rand(1,3,640,640)

onnx_model = './weights/yolov5s.onnx'

dynamic_axes = {'input': {0: 'batch_size', 2: 'height', 3: 'width'},
                'output': {0: 'batch_size', 2: 'height', 3: 'width'}}

torch.onnx.export(model,x,onnx_model,input_names=['input1'],output_names=['output1'], dynamic_axes=dynamic_axes, verbose=True)