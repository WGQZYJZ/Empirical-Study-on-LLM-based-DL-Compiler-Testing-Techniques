import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.rand(10, 10)
lower_cholesky_transform = torch.distributions.transforms.LowerCholeskyTransform(cache_size=0)