import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(5, 5)
input_tensor_triu = torch.Tensor.triu(input_tensor, diagonal=0)