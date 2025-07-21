import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 3, dtype=torch.float64, requires_grad=True)
(eigen_values, eigen_vectors) = torch.eig(input, eigenvectors=True)
eigen_values = torch.eig(input, eigenvectors=False)