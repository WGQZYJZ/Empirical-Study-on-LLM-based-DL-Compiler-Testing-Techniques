import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([3, 6, 8, 10, 12])
other = torch.tensor([2, 5, 7, 11, 13])
output = torch.lcm(input, other)