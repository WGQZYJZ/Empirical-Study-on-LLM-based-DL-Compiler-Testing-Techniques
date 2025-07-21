import torch
from torch import nn
from torch.autograd import Variable
A = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]], dtype=torch.float32)
tau = torch.tensor([1.0], dtype=torch.float32)
out = torch.linalg.householder_product(A, tau)