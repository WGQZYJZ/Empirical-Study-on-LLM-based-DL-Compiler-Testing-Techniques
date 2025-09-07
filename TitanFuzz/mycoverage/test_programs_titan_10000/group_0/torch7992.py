import torch
from torch import nn
from torch.autograd import Variable

X = torch.randn(100, 3)
lower_cholesky = torch.distributions.transforms.LowerCholeskyTransform(cache_size=0)