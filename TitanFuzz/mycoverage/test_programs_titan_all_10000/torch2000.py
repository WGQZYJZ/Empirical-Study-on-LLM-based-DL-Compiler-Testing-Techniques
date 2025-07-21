import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(1, 1)
other = torch.randn(1, 1)
output_tensor = torch.Tensor.logaddexp2(input_tensor, other)