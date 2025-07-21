import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(2, 3, 4)
output = torch.repeat_interleave(input, repeats=3, dim=2)