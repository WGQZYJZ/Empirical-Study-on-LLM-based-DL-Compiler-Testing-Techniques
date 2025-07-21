import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 3)
(eigenvalues, eigenvectors) = torch.symeig(input, eigenvectors=True)