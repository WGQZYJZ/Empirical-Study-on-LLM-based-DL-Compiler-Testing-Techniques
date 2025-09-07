import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 3)
output_tensor = torch.Tensor.sigmoid_(input_tensor)
input_tensor = torch.randn(3, 3)
output_tensor = torch.Tensor.tanh_(input_tensor)
input_tensor = torch.randn(3, 3)