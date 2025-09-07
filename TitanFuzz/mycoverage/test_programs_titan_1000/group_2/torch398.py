import torch
from torch import nn
from torch.autograd import Variable
A = torch.rand(4, 4)
cond_A = torch.linalg.cond(A)