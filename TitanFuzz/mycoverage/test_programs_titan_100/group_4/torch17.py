import torch
from torch import nn
from torch.autograd import Variable
A = torch.rand(3, 3)
tau = torch.rand(3)
torch.linalg.householder_product(A, tau)