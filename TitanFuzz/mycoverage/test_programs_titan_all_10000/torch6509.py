import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 2)
(eigen_values, eigen_vectors) = torch.eig(input, True)
eigen_values = torch.eig(input, False)