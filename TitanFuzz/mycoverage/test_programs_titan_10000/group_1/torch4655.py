import torch
from torch import nn
from torch.autograd import Variable

A = torch.rand(10, 20)
A = torch.rand(10, 20)
(U, S, V) = torch.pca_lowrank(A, q=None, center=True, niter=2)