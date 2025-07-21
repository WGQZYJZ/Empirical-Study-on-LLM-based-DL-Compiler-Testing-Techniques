import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3, 4, 4, 4)
output_data = torch.nn.ConstantPad3d((0, 0, 0, 0, 1, 1), 0)(input_data)