import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.randn(4)
output_tensor = torch.Tensor.ceil_(input_tensor)