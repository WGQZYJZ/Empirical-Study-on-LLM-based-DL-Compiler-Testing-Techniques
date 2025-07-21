import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 3, 224, 224)
model = torch.hub.load('pytorch/vision:v0.6.0', 'resnet50', pretrained=True)
model.eval()
with torch.no_grad():
    output = model(input_data)