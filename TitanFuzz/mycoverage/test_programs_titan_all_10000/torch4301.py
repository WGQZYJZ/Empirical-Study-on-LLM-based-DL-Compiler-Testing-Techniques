import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 3)
cholesky_result = torch.Tensor.cholesky(input_tensor)