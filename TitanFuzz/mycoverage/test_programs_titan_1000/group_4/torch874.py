import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 3)
torch.mean(input, dim=1, keepdim=False)
input = torch.randn(3, 3)
torch.mean(input, dim=1, keepdim=True)