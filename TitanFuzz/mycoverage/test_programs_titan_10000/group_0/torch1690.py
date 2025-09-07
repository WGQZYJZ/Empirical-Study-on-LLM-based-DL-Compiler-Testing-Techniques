import torch
from torch import nn
from torch.autograd import Variable

A = torch.randn(3, 3)
(e, v) = torch.eig(A, eigenvectors=True)
(u, s, v) = torch.svd(A, some=True)