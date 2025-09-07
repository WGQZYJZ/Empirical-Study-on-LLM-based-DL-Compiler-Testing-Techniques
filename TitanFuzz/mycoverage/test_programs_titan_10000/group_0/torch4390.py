import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.randn(2, 2)
cholesky_inverse = torch.Tensor.cholesky_inverse(input_tensor)