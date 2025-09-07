import torch
from torch import nn
from torch.autograd import Variable

x = torch.randn(10, 3)
linear_layer = torch.nn.Linear(3, 4)
y = linear_layer(x)
linear_layer = torch.nn.Linear(3, 4, bias=False)
linear_layer = torch.nn.Linear(3, 4, bias=False)