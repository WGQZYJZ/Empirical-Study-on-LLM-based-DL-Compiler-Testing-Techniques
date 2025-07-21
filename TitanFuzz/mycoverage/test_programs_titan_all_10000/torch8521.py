import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(1, 2, 3, 4)
y = torch.rand(1, 2, 3, 4)
z = torch.allclose(x, y, rtol=1e-05, atol=1e-08, equal_nan=False)