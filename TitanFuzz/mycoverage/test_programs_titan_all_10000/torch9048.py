import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([[[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]]])
output = torch.nn.ConstantPad2d((1, 1, 1, 1), 3)(input)