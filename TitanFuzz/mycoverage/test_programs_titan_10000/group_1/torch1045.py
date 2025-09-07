import torch
from torch import nn
from torch.autograd import Variable

A = torch.rand(5, 5)
torch.linalg.inv_ex(A)