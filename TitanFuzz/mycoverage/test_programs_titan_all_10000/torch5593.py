import torch
from torch import nn
from torch.autograd import Variable
A = torch.rand(3, 3)
B = torch.linalg.inv_ex(A)
C = torch.linalg.inv_ex(A, check_errors=True, out=None)