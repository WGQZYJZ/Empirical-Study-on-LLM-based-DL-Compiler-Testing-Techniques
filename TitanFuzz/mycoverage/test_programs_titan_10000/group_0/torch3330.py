import torch
from torch import nn
from torch.autograd import Variable

x = torch.linspace(0, 10, steps=5)
y = torch.sin(x)