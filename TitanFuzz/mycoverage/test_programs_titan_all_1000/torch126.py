import torch
from torch import nn
from torch.autograd import Variable
A = torch.randn(2, 3, requires_grad=True)
B = torch.linalg.pinv(A)