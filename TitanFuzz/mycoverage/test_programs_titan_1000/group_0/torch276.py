import torch
from torch import nn
from torch.autograd import Variable
abs = torch.rand(4, 4)
angle = torch.rand(4, 4)
out = torch.polar(abs, angle)