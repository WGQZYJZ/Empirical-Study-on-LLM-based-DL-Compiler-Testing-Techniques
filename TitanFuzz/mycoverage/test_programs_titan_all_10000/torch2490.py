import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 3, 224, 224)
model = torch.hub.load('pytorch/vision:v0.6.0', 'resnet18', pretrained=True)
model.eval()
output = model(input_data)