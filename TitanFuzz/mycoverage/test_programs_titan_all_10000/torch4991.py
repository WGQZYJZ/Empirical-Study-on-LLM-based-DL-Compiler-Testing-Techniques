import torch
from torch import nn
from torch.autograd import Variable
A = torch.randn(10, 10)
(U, S, V) = torch.svd_lowrank(A, q=6, niter=2, M=None)