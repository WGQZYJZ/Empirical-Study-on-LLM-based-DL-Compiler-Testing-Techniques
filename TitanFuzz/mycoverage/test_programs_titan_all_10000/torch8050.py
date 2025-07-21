import torch
from torch import nn
from torch.autograd import Variable
A = torch.Tensor([[1, 2], [3, 4]])
torch.linalg.slogdet(A)
A = torch.Tensor([[1, 2], [3, 4]])
b = torch.Tensor([[1, 2], [3, 4]])
torch.linalg.solve(b, A)