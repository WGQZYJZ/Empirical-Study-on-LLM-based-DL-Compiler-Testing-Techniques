import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(1, 2, 3)
result = torch.Tensor.digamma_(input_tensor)