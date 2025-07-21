import torch
from torch import nn
from torch.autograd import Variable
a = torch.Tensor([[1, 2], [3, 4]])
(eigenvalues, eigenvectors) = torch.eig(a, True)