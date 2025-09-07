import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 1, 100)
output_data = torch.kaiser_window(100, periodic=True, beta=12.0)