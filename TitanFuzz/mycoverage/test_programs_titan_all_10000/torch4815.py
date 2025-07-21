import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(1, 2, 3, 4)
output = torch.conj(input)