import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 4)
output_tensor = torch.Tensor.to_sparse(input_tensor, sparse_dim=1)