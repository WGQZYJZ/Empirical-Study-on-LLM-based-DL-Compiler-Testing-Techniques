import torch
from torch import nn
from torch.autograd import Variable
N = 3
M = 4
K = 5
A = torch.randn(N, M)
B = torch.randn(M, K)
C = torch.einsum('ij,jk->ik', A, B)