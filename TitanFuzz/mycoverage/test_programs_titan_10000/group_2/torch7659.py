import torch
from torch import nn
from torch.autograd import Variable

A = Variable(torch.Tensor([[1, 2], [3, 4]]), requires_grad=False)
eigvals = torch.linalg.eigvals(A)