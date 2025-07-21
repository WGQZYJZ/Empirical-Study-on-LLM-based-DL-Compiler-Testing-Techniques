import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(3, 3)
model = torch.hub.load('pytorch/vision:v0.6.0', 'resnet18', pretrained=True)
model.eval()