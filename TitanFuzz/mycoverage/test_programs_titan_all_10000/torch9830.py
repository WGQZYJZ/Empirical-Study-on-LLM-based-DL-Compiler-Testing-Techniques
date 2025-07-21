import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(3, 3)
y = torch.rand(3, 3)
z = torch.rand(3, 3)
torch.jit.fork(torch.add, x, y, out=z)
torch.jit.fork(torch.add, x, y, out=z)
torch.jit.fork(torch.add, x, y, out=z)
torch.jit.fork(torch.add, x, y, out=z)