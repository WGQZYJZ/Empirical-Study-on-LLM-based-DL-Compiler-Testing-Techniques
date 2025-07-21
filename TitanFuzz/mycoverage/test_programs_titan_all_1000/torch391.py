import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(10, 5)
cummin_result = torch.cummin(input_data, dim=0)