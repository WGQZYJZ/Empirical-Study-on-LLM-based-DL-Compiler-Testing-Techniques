import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 2)
output_tensor = torch.Tensor.not_equal(input_tensor, 0.5)