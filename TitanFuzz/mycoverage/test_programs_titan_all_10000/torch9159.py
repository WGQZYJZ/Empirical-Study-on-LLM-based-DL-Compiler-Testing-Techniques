import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(2, 3)
output = torch.deg2rad(input)