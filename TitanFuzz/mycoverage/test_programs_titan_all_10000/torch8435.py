import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(20, 16, 50, 32, 45)
max_pooling_layer = torch.nn.MaxPool3d(kernel_size=2)
output = max_pooling_layer(input)