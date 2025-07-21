import torch
from torch import nn
from torch.autograd import Variable
abs = torch.randn(4, 4)
angle = torch.randn(4, 4)
out = torch.polar(abs, angle)