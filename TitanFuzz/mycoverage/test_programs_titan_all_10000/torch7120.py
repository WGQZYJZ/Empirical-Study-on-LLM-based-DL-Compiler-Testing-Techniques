import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(1, 1, 3, 3)
y = torch.rand(1, 1, 3, 3)
x = torch.jit.annotate(torch.Tensor, x)
y = torch.jit.annotate(torch.Tensor, y)