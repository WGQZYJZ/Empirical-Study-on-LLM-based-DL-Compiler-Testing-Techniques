import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(4)
other = torch.randn(4)
out = torch.nextafter(input, other)
out = torch.nextafter(input, other, out=torch.empty_like(input))