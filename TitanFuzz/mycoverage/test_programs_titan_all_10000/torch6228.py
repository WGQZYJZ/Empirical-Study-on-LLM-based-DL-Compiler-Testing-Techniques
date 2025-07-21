import torch
from torch import nn
from torch.autograd import Variable
x = torch.linspace(0, 10, 5)
x = torch.logspace(start=(- 10), end=10, steps=5)
x = torch.eye(4)