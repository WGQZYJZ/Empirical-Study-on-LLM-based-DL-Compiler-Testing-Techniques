import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(1, 3, 2)
output_tensor = torch.Tensor.clip_(input_tensor, min=(- 0.5), max=0.5)