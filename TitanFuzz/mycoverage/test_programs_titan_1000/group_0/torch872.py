import torch
from torch import nn
from torch.autograd import Variable
A = torch.rand(3, 3, requires_grad=True)
B = torch.rand(3, 3, requires_grad=True)
C = torch.rand(3, 3, requires_grad=True)
D = torch.linalg.multi_dot([A, B, C])