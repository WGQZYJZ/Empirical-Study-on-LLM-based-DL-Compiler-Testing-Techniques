import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(10, 5)
torch.var_mean(input, dim=0, unbiased=True, keepdim=False)
torch.var_mean(input, dim=0, unbiased=False, keepdim=False)
torch.var_mean(input, dim=0, unbiased=True, keepdim=True)
torch.var_mean(input, dim=1, unbiased=True, keepdim=True)