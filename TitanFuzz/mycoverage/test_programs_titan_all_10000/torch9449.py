import torch
from torch import nn
from torch.autograd import Variable
A = torch.randn(3, 3)
(eigen_values, eigen_vectors) = torch.linalg.eig(A)