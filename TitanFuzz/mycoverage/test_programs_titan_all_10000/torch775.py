import torch
from torch import nn
from torch.autograd import Variable
A = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
result = torch.linalg.det(A)
out = torch.empty(1)
torch.linalg.det(A, out=out)