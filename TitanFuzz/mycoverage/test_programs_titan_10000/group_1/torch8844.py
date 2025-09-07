import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.randn(2, 3)
output = torch.Tensor.arcsin_(input_tensor)
output = torch.arcsin_(input_tensor)