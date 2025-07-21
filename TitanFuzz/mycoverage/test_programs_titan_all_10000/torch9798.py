import torch
from torch import nn
from torch.autograd import Variable
input_data = Variable(torch.randn(1, 10))
linear_layer = torch.nn.Linear(10, 1)
output = linear_layer(input_data)