import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(1, 1, 3)
y = torch.kaiser_window(3, periodic=True, beta=12.0)
z = torch.kaiser_window(3, periodic=True, beta=12.0, dtype=torch.float64)