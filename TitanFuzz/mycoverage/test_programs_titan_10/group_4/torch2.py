import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(4, 4)
sparse_dim = torch.Tensor.sparse_dim(input_tensor)