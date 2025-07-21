import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3)
output_tensor = torch.Tensor.conj_physical(input_tensor)