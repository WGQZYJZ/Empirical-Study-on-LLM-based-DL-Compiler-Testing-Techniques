import torch
from torch import nn
from torch.autograd import Variable
A = torch.randn(2, 2)
(eigen_values, eigen_vectors) = torch.linalg.eigh(A)