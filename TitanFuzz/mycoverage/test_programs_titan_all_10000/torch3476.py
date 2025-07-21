import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 1, 3, 3)
padding = (0, 1, 1, 0)
zero_pad_layer = torch.nn.ZeroPad2d(padding)
output_data = zero_pad_layer(Variable(input_data))