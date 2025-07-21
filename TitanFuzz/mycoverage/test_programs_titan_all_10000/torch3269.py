import torch
from torch import nn
from torch.autograd import Variable
A = torch.randn(2, 2)
eigenvalues = torch.linalg.eigvals(A)