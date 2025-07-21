import torch
from torch import nn
from torch.autograd import Variable
A = torch.randn(3, 3)
A_pinv = torch.linalg.pinv(A)
torch.allclose(torch.mm(A, A_pinv), torch.eye(3))
torch.allclose(torch.mm(A_pinv, A), torch.eye(3))