import torch
from torch import nn
from torch.autograd import Variable
A = torch.randn(4, 3)
x = torch.randn(3)
b = torch.randn(4)
out = torch.addmv(b, A, x)
out = torch.addmv(b, A, x, alpha=0.5)
out = torch.addmv(b, A, x, alpha=0.5, beta=2)
out = torch.addmv(b, A, x, alpha=0.5, beta=2, out=b)