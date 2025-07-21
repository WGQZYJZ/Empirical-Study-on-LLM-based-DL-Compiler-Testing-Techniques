import torch
from torch import nn
from torch.autograd import Variable
A = torch.randn(10, 3, 5)
result = torch.linalg.vector_norm(A, dim=1)