import torch
from torch import nn
from torch.autograd import Variable
x = torch.ones(2, 2, requires_grad=True)
torch.set_grad_enabled(True)
y = (x + 2)
z = ((y * y) * 3)
out = z.mean()
torch.set_grad_enabled(False)
a = torch.randn(2, 2)
a = ((a * 3) / (a - 1))
a.requires_grad_(True)
b = (a * a).sum()