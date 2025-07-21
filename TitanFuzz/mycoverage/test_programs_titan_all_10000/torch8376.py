import torch
from torch import nn
from torch.autograd import Variable
A = torch.randn(3, 3)
A = A.mm(A.t())
(e, V) = torch.linalg.eigh(A)