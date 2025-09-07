import torch
from torch import nn
from torch.autograd import Variable
A = torch.rand(5, 5)
(eigvals, eigvecs) = torch.linalg.eigh(A)