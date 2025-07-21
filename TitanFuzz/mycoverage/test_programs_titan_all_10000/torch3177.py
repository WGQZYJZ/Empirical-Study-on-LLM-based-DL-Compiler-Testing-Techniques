import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(3, 2)
result = torch.Tensor.subtract_(input_tensor, other=0.5)
result = torch.Tensor.subtract_(input_tensor, other=0.5, alpha=0.5)