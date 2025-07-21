import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(10, 10)
input = input.mm(input.transpose(0, 1))
(eigenvalues, eigenvectors) = torch.symeig(input, eigenvectors=True)