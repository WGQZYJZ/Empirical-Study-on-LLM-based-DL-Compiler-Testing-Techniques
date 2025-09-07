import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 3)
(eigen_values, eigen_vectors) = torch.symeig(input, eigenvectors=True)