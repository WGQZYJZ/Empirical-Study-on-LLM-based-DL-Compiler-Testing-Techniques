import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(1, 3, 224, 224)
model = torch.hub.load('pytorch/vision:v0.6.0', 'resnet18', pretrained=True)
model.eval()
y = model(x)