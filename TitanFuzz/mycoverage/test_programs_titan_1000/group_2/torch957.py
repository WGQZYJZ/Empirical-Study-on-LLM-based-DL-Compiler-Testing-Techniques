import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(3, 4, 5, 6)
output_data = torch.flatten(input_data, start_dim=1, end_dim=(- 1))