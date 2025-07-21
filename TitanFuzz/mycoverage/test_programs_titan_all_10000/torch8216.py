import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(20, 16, 50)
max_pooling_layer = torch.nn.MaxPool1d(3, stride=2)
output = max_pooling_layer(input)