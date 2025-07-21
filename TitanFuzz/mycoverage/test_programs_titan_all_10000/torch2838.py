import torch
from torch import nn
from torch.autograd import Variable
A = torch.randn(3, 3)
tau = torch.randn(3)
torch.linalg.householder_product(A, tau)
torch.linalg.householder_product(A, tau, out=A)