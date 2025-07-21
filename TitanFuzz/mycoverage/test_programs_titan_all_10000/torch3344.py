import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(10)
output_tensor = torch.Tensor.exponential_(input_tensor, lambd=1, generator=None)