import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 3, 4, 5)
output_data = torch.atanh(input_data)