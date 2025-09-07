import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(10, 3, 3)
output_tensor = torch.Tensor.resolve_neg(input_tensor)