import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3, 5)
output_data = torch.swapdims(input_data, 0, 1)