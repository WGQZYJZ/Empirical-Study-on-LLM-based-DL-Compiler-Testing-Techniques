import torch
from torch import nn
from torch.autograd import Variable
A = torch.randn(3, 2)
(U, S, V) = torch.linalg.svd(A)