import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(5, 3)
y = torch.rand(5, 3)
result = torch.empty(5, 3)
torch.add(x, y, out=result)
y.add_(x)