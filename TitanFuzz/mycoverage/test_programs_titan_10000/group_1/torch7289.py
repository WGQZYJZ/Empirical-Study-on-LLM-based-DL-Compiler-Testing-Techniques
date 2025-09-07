import torch
from torch import nn
from torch.autograd import Variable

x = torch.randn(1, requires_grad=True)
with torch.no_grad():
    y = (x * 2)