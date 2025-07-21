import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 3)
output_tensor = torch.Tensor.arctan_(input_tensor)