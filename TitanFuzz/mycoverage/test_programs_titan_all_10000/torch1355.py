import torch
from torch import nn
from torch.autograd import Variable
A = torch.rand(3, 5)
B = torch.rand(5, 3)
torch.einsum('ij, jk -> ik', A, B)
torch.einsum('ij, jk -> ik', A, B)
torch.einsum('ij, jk -> ik', A, B)
torch.einsum('ij, jk -> ik', A, B)
torch.einsum('ij, jk -> ik', A, B)