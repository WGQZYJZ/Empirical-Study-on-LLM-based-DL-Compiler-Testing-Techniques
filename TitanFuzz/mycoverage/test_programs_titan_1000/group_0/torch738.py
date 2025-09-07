import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(1, 3, 10, 10)
output_tensor = torch.Tensor.clip_(input_tensor, min=(- 1), max=1)
input_tensor = torch.randn(1, 3, 10, 10)
output_tensor = torch.Tensor.clamp_(input_tensor, min=(- 1), max=1)