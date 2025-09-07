import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(1, 1)
output_tensor = torch.Tensor.arctan(input_tensor)