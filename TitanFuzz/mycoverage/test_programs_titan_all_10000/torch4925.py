import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(4, 4)
output_tensor = torch.Tensor.reciprocal(input_tensor)
input_tensor = torch.randn(4, 4)
output_tensor = torch.Tensor.round(input_tensor)