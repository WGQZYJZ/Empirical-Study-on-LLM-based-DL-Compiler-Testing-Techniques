import torch
from torch import nn
from torch.autograd import Variable
A = torch.randn(3, 3)
torch.linalg.det(A)
torch.linalg.det(A, out=torch.zeros(1))
torch.linalg.det(A, out=torch.zeros(1, 1))
torch.linalg.det(A, out=torch.zeros(1, 1, 1))
torch.linalg.det(A, out=torch.zeros(1, 1, 1, 1))
torch.linalg.det