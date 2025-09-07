import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(5, 5)
cummin_result = torch.cummin(input, dim=1)