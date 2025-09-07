import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 4)
output_data = torch.floor(input_data)