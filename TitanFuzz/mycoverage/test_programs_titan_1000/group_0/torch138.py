import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(4, 3)
output = torch.nn.functional.normalize(input, p=2.0, dim=1, eps=1e-12, out=None)