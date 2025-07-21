import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3, 4)
output_data = torch.moveaxis(input_data, 2, 0)
output_data = torch.moveaxis(input_data, 1, 2)