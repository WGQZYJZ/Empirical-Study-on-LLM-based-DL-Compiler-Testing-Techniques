import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(5, 3)
y = torch.rand(5, 3)
z = torch.add(x, y)
result = torch.empty(5, 3)
torch.add(x, y, out=result)
y.add_(x)
x = torch.randn(4, 4)
y = x.view(16)
z = x.view((- 1), 8)
x = torch.randn(1)
a = torch.ones(5)
b = a.numpy()
a.add_(1)