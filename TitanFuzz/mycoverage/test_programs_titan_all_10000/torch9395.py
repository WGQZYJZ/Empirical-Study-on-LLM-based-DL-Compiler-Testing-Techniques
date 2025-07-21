import torch
from torch import nn
from torch.autograd import Variable
A = torch.randn(3, 3, dtype=torch.float)
B = torch.randn(3, 1, dtype=torch.float)
X = torch.linalg.lstsq(A, B)