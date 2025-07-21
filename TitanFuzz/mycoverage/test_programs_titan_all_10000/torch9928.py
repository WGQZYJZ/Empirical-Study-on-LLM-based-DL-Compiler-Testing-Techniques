import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3)
mat = torch.randn(3, 4)
torch.Tensor.smm(input_tensor, mat)