import torch
from torch import nn
from torch.autograd import Variable
tensor_one = torch.rand(3, 3)
tensor_two = torch.rand(3, 3)
tensor_three = torch.rand(3, 3)
lower_cholesky_transform = torch.distributions.transforms.LowerCholeskyTransform(cache_size=0)