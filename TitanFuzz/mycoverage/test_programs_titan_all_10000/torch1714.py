import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(4, 3, dtype=torch.float32)
mat = torch.randn(4, 3, dtype=torch.float32)
vec = torch.randn(3, dtype=torch.float32)
torch.Tensor.addmv_(input_tensor, mat, vec, beta=1, alpha=1)