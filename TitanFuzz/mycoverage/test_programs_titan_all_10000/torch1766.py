import torch
from torch import nn
from torch.autograd import Variable
a = torch.logspace(start=0.1, end=2, steps=5, base=2)
b = torch.zeros_like(a)
c = torch.ones(5, 3)
d = torch.zeros(3, 2)
e = torch.ones(3, 2)
f = torch.rand(3, 2)
g = torch.rand(3, 2)