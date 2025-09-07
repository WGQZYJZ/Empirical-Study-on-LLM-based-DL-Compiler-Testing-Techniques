import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 10)
output_data = torch.cosh(input_data)