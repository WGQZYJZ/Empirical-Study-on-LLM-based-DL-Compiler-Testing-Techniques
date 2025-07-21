import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(1, 2, 3)
output_tensor = torch.Tensor.swapdims(input_tensor, 0, 1)