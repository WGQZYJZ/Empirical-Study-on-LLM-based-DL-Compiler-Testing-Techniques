import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(5, 5)
output_tensor = torch.Tensor.narrow_copy(input_tensor, 0, 1, 3)