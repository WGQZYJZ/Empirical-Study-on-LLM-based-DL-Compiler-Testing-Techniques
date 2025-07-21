import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(4, 4)
output_tensor = torch.Tensor.polygamma(input_tensor, 3)
input_tensor = torch.randn(4, 4)
output_tensor = torch.Tensor.pow(input_tensor, 3)