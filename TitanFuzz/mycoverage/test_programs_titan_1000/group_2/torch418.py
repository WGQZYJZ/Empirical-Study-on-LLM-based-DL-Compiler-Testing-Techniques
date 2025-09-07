import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(5, 3)
other_data = torch.randn(5, 3)
result = torch.Tensor.sub_(input_data, other_data)