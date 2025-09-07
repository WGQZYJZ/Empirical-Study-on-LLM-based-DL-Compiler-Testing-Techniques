import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.rand(5, 3)
mat = torch.rand(3, 5)
vec = torch.rand(5)
torch.Tensor.addmv(input_tensor, mat, vec)