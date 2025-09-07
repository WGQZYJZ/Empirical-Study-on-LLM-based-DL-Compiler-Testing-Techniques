import torch
from torch import nn
from torch.autograd import Variable

A = torch.randn(100, 100)
A = torch.mm(A, A.t())
(eigvals, eigvecs) = torch.lobpcg(A, k=10)