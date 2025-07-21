import torch
from torch import nn
from torch.autograd import Variable
A = torch.randn(4, 4)
eigenvalues = torch.linalg.eigvals(A)