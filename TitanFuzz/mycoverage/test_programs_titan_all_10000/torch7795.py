import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(20, 16, 50, 32, 32)
max_pooling_layer = torch.nn.MaxPool3d(kernel_size=2, stride=2)
output = max_pooling_layer(input_data)