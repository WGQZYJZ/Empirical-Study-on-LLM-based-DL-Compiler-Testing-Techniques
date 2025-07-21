import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(2, 3)
frac_output = torch.frac(input)