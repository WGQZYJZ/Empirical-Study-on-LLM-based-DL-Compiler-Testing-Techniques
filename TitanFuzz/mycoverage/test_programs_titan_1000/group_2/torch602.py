import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(3, requires_grad=True)
y = torch.randn(3, requires_grad=True)
z = torch.randn(3, requires_grad=True)
q = torch.true_divide(x, y)
r = torch.true_divide(x, z)
q_out = torch.empty(3)
r_out = torch.empty(3)
torch.true_divide(x, y, out=q_out)
torch.true_divide(x, z, out=r_out)