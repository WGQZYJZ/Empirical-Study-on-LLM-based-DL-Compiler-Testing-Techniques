import torch
from torch import nn
from torch.autograd import Variable
A = torch.randn(2, 2)
A_t = A.t()
A_sym = torch.matmul(A_t, A)
L_sym = torch.linalg.cholesky(A_sym, upper=False)