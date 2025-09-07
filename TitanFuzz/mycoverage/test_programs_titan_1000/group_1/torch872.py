import torch
from torch import nn
from torch.autograd import Variable
x = Variable(torch.randn(1, 1), requires_grad=True)
y = Variable(torch.randn(1, 1), requires_grad=True)
z = Variable(torch.randn(1, 1), requires_grad=True)
a = (x + y)
b = (a + z)
b.backward()
torch.nn.utils.clip_grad_norm_(x, max_norm=1)
torch.nn.utils.clip_grad_norm_(y, max_norm=1)
torch.nn.utils.clip_grad_norm_(z, max_norm=1)