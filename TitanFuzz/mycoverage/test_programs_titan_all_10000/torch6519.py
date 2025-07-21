import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(1, 3, 3)
output_tensor = torch.Tensor.arctan_(input_tensor)