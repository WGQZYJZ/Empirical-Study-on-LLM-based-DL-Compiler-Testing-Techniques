import torch
from torch import nn
from torch.autograd import Variable
A = torch.tensor([[1, 2, 3], [4, 5, 6]])
B = torch.tensor([[1, 2], [3, 4], [5, 6]])
C = torch.chain_matmul(A, B)
D = torch.chain_matmul(A, B, A)
E = torch.chain_matmul(A, B, A, B)
F = torch.chain_matmul(A, B, A, B, A)