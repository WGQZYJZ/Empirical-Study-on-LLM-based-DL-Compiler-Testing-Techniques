import torch
from torch import nn
from torch.autograd import Variable
A = torch.rand(2, 2)
A_t = A.t()
A_sym = torch.mm(A_t, A)
(e, v) = torch.linalg.eigh(A_sym)
A = torch.rand(2, 2)
A_t = A.t()
A_sym = torch.mm(A_t, A)
(e, v) = torch.linalg.eig(A_sym)