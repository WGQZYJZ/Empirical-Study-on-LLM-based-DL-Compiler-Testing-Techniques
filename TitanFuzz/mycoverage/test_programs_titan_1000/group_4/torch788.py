import torch
from torch import nn
from torch.autograd import Variable
A = torch.randn(5, 5)
torch.pca_lowrank(A, q=None, center=True, niter=2)