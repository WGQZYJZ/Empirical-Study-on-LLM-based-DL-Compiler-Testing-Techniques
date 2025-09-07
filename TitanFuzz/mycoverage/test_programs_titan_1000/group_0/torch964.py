import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(10, 3)
torch.quantile(input_data, 0.5, dim=1)
torch.quantile(input_data, 0.5, dim=0)
torch.quantile(input_data, 0.5)