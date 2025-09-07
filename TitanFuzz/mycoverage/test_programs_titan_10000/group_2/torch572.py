import torch
from torch import nn
from torch.autograd import Variable

A = np.random.rand(5, 5)
A = torch.tensor(A)
(U, S, V) = torch.pca_lowrank(A, q=None, center=True, niter=2)