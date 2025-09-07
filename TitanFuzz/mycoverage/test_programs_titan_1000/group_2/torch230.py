import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(3, 3)
relu = torch.nn.ReLU()
y = relu(x)