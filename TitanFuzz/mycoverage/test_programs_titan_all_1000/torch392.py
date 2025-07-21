import torch
from torch import nn
from torch.autograd import Variable
A = torch.randn(3, 3, dtype=torch.float64, requires_grad=True)
A_inv = torch.inverse(A)