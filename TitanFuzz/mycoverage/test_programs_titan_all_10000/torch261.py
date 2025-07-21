import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(1, 2, 3)
output_tensor = torch.Tensor.polygamma_(input_tensor, 3)