import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 4)
output_tensor = torch.Tensor.cov(input_tensor)
output_tensor = torch.Tensor.cov(input_tensor, correction=0)