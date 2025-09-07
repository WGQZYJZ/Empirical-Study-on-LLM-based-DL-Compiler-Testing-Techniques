import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 1, 5, 5, 5)
conv3d = torch.nn.Conv3d(1, 1, 3, stride=1, padding=0)
output = conv3d(input_data)