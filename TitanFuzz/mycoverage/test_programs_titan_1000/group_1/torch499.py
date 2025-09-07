import torch
from torch import nn
from torch.autograd import Variable
A = torch.randn(10, 10)
result = torch.linalg.vector_norm(A, ord=2, dim=None, keepdim=False, dtype=None, out=None)