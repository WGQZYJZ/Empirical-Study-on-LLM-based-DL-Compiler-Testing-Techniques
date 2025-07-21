import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(5, 5)
(eigenvalues, eigenvectors) = torch.symeig(input, eigenvectors=True)