import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(1, 2, 3)
mat = torch.randn(3, 3)
vec = torch.randn(3)
torch.Tensor.addmv(input_tensor, mat, vec, beta=1, alpha=1)