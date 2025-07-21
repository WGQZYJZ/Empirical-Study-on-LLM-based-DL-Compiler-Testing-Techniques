import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(4, 4)
output = torch.narrow(input, 0, 0, 2)