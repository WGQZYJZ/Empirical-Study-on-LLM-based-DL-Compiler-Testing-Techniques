import torch
from torch import nn
from torch.autograd import Variable
a = torch.randn(3, 3)
b = torch.clamp(a, min=0, max=1)