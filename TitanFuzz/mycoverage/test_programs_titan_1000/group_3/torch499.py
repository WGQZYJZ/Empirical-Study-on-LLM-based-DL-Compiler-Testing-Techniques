import torch
from torch import nn
from torch.autograd import Variable
A = torch.randn(3, 3)
A = (A @ A.t())
(eigenvalues, eigenvectors) = torch.linalg.eigh(A)