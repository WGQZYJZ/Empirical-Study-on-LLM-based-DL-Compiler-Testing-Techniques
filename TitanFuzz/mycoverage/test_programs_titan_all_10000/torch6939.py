import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 3)
torch.Tensor.trace(input_tensor)
input_tensor = torch.randn(3, 3)
dim0 = 0
dim1 = 1
torch.Tensor.transpose(input_tensor, dim0, dim1)