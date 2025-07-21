import torch
from torch import nn
from torch.autograd import Variable
A = torch.tensor([[1, 0, 0, 1], [1, 0, 1, 0], [1, 1, 0, 0]], dtype=torch.uint8)
B = torch.tensor([[1, 1, 1, 0], [1, 0, 1, 1], [0, 0, 1, 1]], dtype=torch.uint8)
C = torch.bitwise_and(A, B)
D = torch.bitwise_or(A, B)
E = torch.bitwise_xor(A, B)