import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(4, 6)
output_tensor = torch.vsplit(input_tensor, 2)