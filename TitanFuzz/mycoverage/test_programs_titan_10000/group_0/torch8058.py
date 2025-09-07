import torch
from torch import nn
from torch.autograd import Variable

A = torch.randn(3, 2)
rank = torch.linalg.matrix_rank(A)