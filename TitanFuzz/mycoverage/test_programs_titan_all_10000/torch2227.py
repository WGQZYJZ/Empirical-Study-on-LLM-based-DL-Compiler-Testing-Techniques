import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(1, requires_grad=True)
output = torch.deg2rad(input)