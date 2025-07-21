import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(1, 2, 3, 4, 5)
torch.Tensor.arccosh_(input_tensor)