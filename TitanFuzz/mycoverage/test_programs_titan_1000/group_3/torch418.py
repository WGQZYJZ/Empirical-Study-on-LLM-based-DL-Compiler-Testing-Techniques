import torch
from torch import nn
from torch.autograd import Variable
x = torch.arange(1, 10, dtype=torch.float)
y = torch.logspace(start=0, end=2, steps=5)