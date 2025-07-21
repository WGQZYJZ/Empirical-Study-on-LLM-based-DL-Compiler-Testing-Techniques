import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(4, 4)
value = torch.rand(1)
output_tensor = torch.Tensor.multiply(input_tensor, value)
input_tensor = torch.rand(4, 4)
value = torch.rand(1)
output_tensor = torch.Tensor.mul(input_tensor, value)