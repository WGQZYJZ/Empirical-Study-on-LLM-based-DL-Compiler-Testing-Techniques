import torch
from torch import nn
from torch.autograd import Variable
A = torch.randn(3, 3)
B = torch.linalg.inv(A)