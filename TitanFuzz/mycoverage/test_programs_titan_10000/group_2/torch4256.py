import torch
from torch import nn
from torch.autograd import Variable

x = torch.randn(1, 3, dtype=torch.float)
y = torch.randn(1, 3, dtype=torch.float)
out = torch.xlogy(x, y)