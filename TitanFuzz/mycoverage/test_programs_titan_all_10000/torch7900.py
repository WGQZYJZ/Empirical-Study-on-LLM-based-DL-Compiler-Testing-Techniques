import torch
from torch import nn
from torch.autograd import Variable
y = torch.arange(1, 5, dtype=torch.float64)
dx = torch.tensor(0.25, dtype=torch.float64)
result = torch.trapezoid(y, dx=dx)