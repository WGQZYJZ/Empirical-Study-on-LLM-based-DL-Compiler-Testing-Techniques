import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 3)
output = torch.Tensor.is_conj(input_tensor)