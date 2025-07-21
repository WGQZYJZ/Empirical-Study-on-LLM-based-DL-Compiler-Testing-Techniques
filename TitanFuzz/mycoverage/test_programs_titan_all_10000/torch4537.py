import torch
from torch import nn
from torch.autograd import Variable
A = torch.rand(2, 2)
slogdet = torch.linalg.slogdet(A)