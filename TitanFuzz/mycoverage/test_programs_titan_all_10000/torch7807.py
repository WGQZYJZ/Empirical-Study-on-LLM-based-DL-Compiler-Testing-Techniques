import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 5, 5)
tau = torch.randn(3, 5)
torch.orgqr(input, tau)
torch.orgqr(input, tau, out=input)
input = torch.randn(4, 5)
torch.pdist(input, p=2)
input = torch.randn(3, 5, 5)