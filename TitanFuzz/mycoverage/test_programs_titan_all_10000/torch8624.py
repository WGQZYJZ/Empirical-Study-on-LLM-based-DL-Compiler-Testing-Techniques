import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]])
pad = torch.nn.ConstantPad1d((2, 3), 0)
output = pad(input)
input = torch.tensor([[[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]])
pad = torch.nn.ConstantPad2d((1, 2, 3, 4), 0)
output = pad(input)