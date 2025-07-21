import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 3, 3, 1)
output_data = torch.squeeze(input_data, dim=(- 1))
output_data = torch.squeeze(input_data, dim=1)