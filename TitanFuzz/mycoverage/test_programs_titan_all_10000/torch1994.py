import torch
from torch import nn
from torch.autograd import Variable
(n, d, r) = (1000, 10, 5)
A = torch.randn(n, d, dtype=torch.float64)
q = torch.pca_lowrank(A, q=r, center=True, niter=2)