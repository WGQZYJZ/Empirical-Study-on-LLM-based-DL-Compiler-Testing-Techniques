import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([0, 2, 4, 6, 8])
other = torch.tensor([1, 2, 3, 4, 5])
output = torch.bitwise_left_shift(input, other)