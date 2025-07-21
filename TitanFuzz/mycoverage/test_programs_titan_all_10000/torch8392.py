import torch
from torch import nn
from torch.autograd import Variable
abs = torch.randn(2, 3)
angle = torch.randn(2, 3)
out = torch.polar(abs, angle)