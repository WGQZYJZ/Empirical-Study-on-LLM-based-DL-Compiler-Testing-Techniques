import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(100)
output_data = torch.erfc(input_data)