import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(20, 16, 50, 32, 45)
avgpool3d = torch.nn.AvgPool3d(kernel_size=2, stride=2, padding=0)
output = avgpool3d(input)