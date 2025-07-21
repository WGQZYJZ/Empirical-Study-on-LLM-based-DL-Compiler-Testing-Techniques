import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(10, 4)
output_data = torch.arctan(input_data)