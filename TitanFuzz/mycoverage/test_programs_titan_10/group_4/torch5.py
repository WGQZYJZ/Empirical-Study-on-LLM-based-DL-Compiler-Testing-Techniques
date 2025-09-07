import torch
from torch import nn
from torch.autograd import Variable
n = 1000
d = 100
A = torch.rand(n, d, dtype=torch.float64)
A = torch.mm(A, A.transpose(0, 1))
(eigvals, eigvecs) = torch.lobpcg(A, k=10)