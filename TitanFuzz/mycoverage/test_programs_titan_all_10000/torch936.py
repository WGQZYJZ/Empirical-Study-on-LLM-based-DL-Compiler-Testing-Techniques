import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(3, 4)
cummin_data = torch.cummin(input_data, dim=1)