import torch
from torch import nn
from torch.autograd import Variable

A = torch.rand(10, 10)
A = A.mm(A.t())
(eig_vals, eig_vecs) = torch.linalg.eigh(A)