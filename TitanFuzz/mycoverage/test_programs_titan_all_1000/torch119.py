import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(1, 10)
y = torch.nn.functional.tanh(x)