import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 3, 7, 7)
flatten = torch.nn.Flatten(start_dim=1, end_dim=(- 1))
output_data = flatten(input_data)
input_data = torch.randn(1, 3, 7, 7)
flatten = torch.nn.Flatten(start_dim=1, end_dim=(- 1))
output_data = flatten(input_data)