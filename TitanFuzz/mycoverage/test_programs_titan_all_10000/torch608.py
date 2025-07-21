import torch
from torch import nn
from torch.autograd import Variable
A = torch.randn(3, 3)
eigvals = torch.linalg.eigvalsh(A)