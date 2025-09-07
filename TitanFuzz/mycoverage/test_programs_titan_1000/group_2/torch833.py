import torch
from torch import nn
from torch.autograd import Variable
A = torch.randn(3, 3)
A = torch.mm(A.t(), A)
B = torch.cholesky_inverse(A)