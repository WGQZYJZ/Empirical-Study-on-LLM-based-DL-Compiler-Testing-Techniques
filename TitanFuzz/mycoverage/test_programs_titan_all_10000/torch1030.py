import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(10, 10)
output = torch.Tensor.is_conj(input_tensor)