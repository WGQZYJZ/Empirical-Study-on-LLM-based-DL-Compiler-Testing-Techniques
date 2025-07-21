import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(1, 4, 5, 6)
output = torch.Tensor.sparse_dim(input_tensor)