import torch
from torch import nn
from torch.autograd import Variable

a = torch.rand(5, 3)
b = torch.rand(3, 4)
c = torch.linalg.matmul(a, b)