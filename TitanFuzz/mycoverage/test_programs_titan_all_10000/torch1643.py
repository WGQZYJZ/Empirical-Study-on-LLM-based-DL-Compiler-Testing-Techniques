import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3, dtype=torch.float)
other = torch.randn(2, 3, dtype=torch.float)
output_tensor = torch.Tensor.greater_equal(input_tensor, other)