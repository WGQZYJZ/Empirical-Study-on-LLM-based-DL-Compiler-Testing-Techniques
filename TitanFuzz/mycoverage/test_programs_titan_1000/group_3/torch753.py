import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 3)
value = 2
output_tensor = torch.Tensor.true_divide(input_tensor, value)