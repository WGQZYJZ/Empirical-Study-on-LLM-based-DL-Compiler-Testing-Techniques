import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(10, 10)
gelu_layer = torch.nn.GELU()
output = gelu_layer(input_data)