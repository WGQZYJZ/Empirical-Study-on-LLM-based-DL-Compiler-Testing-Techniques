import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3, requires_grad=True)
mat = torch.randn(2, 3, requires_grad=True)
vec = torch.randn(3, requires_grad=True)
torch.Tensor.addmv_(input_tensor, mat, vec, beta=1, alpha=1)