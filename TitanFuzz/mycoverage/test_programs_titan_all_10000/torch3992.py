import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 1)
output_data = torch.cos(input_data)