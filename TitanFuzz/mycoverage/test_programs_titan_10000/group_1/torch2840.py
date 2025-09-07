import torch
from torch import nn
from torch.autograd import Variable

a = torch.randn(4, 4)
torch.min(a, 1)
torch.min(a, 1, keepdim=True)
torch.min(a, 1, keepdim=True)[0]
a = torch.randn(4, 4)
torch.min(a, 1)
torch.min(a, 1, keepdim=True)
torch.min(a, 1, keepdim=True)[0]