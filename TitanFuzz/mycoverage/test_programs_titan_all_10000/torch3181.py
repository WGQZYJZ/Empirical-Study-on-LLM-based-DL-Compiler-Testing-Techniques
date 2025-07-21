import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(3, 3)
torch.Tensor.cholesky_inverse(input_tensor, upper=False)