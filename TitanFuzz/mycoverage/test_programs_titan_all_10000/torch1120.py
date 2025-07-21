import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(4, 4)
output_tensor = torch.Tensor.exponential_(input_tensor, lambd=1)