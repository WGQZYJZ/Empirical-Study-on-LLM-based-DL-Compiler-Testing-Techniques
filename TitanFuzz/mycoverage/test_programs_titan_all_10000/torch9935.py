import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(10, 3)
y = torch.nn.functional.normalize(x, p=2.0, dim=1, eps=1e-12, out=None)