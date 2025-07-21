import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(5, 3, dtype=torch.float32)
output_tensor = torch.Tensor.sinh_(input_tensor)