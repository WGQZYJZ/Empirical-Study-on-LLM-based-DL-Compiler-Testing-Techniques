import torch
from torch import nn
from torch.autograd import Variable
A = torch.randn(3, 3, requires_grad=True)
A_inv = torch.linalg.inv(A)