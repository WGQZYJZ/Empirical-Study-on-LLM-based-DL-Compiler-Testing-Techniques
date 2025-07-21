import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(3, 3)
y = torch.rand(3, 3)
x_type = torch.jit.annotate(torch.Tensor, x)
y_type = torch.jit.annotate(torch.Tensor, y)
z = (x + y)
z_type = torch.jit.annotate(torch.Tensor, z)