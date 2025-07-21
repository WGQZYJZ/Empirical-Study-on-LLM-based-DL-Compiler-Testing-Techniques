import torch
from torch import nn
from torch.autograd import Variable
A = torch.arange(6).view(2, 3)
B = torch.arange(6).view(3, 2)
C = torch.einsum('ij,jk->ik', A, B)