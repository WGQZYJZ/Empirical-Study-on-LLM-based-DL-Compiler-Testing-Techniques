import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
padding_layer = torch.nn.ConstantPad2d(2, 0)
output_data = padding_layer(input_data)