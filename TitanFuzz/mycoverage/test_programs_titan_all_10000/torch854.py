import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3)
n = 1
output_tensor = torch.Tensor.polygamma(input_tensor, n)