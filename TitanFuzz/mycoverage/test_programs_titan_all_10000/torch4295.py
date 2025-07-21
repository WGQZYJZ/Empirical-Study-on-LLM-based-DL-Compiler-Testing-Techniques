import torch
from torch import nn
from torch.autograd import Variable
A = torch.randn(3, 3)
A_t = A.t()
A_symm = torch.matmul(A_t, A)
L = torch.linalg.cholesky_ex(A_symm)