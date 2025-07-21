import torch
from torch import nn
from torch.autograd import Variable
A = torch.rand(3, 3)
A = (A.t() @ A)
A = (A + torch.eye(3, 3))
A_np = A.numpy()
A_inv = torch.cholesky_inverse(A)