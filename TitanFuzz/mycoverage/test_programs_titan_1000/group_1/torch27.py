import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 1, 3, 3)
torch.random.manual_seed(1)
conv = torch.nn.Conv2d(1, 1, kernel_size=3, stride=1, padding=1)
torch.nn.init.constant_(conv.weight, 1)
torch.nn.init.constant_(conv.bias, 0)
output_data = conv(input_data)