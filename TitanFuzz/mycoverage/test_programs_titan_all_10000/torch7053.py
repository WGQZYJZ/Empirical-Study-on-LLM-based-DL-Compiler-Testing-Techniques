import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([[True, False, False], [False, False, False]])
y = torch.any(x)
y = torch.any(x, dim=0)
y = torch.any(x, dim=1)
y = torch.any(x, dim=1, keepdim=True)