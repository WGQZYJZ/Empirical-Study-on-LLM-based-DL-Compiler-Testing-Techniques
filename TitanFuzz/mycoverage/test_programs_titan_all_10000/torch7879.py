import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 1, 5, 5)
torch.nn.AdaptiveAvgPool2d(output_size=2)(input)
torch.nn.AdaptiveAvgPool2d(output_size=(2, 2))(input)
torch.nn.AdaptiveAvgPool2d(output_size=(2, 3))(input)
torch.nn.AdaptiveAvgPool2d(output_size=(3, 2))(input)
torch.nn.AdaptiveAvgPool2d(output_size=(3, 3))(input)