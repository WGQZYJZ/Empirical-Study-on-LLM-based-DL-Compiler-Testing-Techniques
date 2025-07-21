import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(10, 8)
input2 = torch.randn(8, 10)
output_tensor = torch.Tensor.orgqr(input_tensor, input2)