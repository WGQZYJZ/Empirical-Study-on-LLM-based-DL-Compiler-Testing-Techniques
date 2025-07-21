import torch
from torch import nn
from torch.autograd import Variable
A = torch.randn(3, 3)
(eig_vals, eig_vecs) = torch.linalg.eig(A)