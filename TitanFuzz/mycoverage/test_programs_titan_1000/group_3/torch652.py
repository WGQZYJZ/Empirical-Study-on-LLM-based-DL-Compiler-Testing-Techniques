import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(1, 3, 3)
output_tensor = torch.Tensor.neg_(input_tensor)
input_tensor = torch.randn(1, 3, 3)
output_tensor = torch.Tensor.nelement(input_tensor)
input_tensor = torch