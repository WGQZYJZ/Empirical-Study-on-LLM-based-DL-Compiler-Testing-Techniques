import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(1, 2, 3, 4, 5)
output_tensor = torch.Tensor.acos_(input_tensor)