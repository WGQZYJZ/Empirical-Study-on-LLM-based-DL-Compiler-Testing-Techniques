import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 4)
q = torch.tensor([0.2, 0.5, 0.9])
torch.quantile(input, q, dim=0)
torch.quantile(input, q, dim=0, keepdim=True)
torch.quantile(input, q, dim=1)
torch.quantile(input, q, dim=1, keepdim=True)