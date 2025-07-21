import torch
from torch import nn
from torch.autograd import Variable
A = torch.randn(1000, 1000)
t1 = time.time()
(U, S, V) = torch.svd(A)
t2 = time.time()
t1 = time.time()
(U, S, V) = torch.svd_lowrank(A, q=6, niter=2, M=None)
t2 = time.time()