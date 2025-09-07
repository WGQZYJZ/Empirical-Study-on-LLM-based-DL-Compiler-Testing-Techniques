import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 3)
(eig_value, eig_vector) = torch.symeig(input, eigenvectors=True)