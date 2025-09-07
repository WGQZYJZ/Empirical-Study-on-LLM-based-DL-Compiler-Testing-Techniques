import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.randn(4, 4)
input_tensor = torch.randn(4, 4)
torch.Tensor.cholesky_inverse(input_tensor, upper=False)