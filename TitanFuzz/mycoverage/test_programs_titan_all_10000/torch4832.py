import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(3, 4, 5)
output_data = torch.swapdims(input_data, 0, 2)