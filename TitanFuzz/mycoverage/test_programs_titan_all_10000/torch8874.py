import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.ones(3, 4)
mat = torch.ones(3, 3)
vec = torch.ones(3)
torch.Tensor.addmv_(input_tensor, mat, vec, beta=1, alpha=1)