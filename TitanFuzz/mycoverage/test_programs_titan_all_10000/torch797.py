import torch
from torch import nn
from torch.autograd import Variable
A = torch.rand(3, 3)
A_inv = torch.linalg.inv(A)
I = torch.mm(A, A_inv)