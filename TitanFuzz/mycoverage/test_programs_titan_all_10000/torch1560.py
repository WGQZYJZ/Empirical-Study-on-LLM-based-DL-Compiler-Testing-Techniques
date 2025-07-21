import torch
from torch import nn
from torch.autograd import Variable
A = Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
(U, S, V) = torch.pca_lowrank(A, q=None, center=True, niter=2)