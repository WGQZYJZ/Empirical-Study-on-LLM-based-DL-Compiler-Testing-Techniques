import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 1, 2, 1, 2)
input_tensor = torch.randn(2, 1, 2, 1, 2)
output_tensor = torch.Tensor.squeeze(input_tensor, dim=1)
input_tensor = torch.randn(2, 1, 2, 1, 2)