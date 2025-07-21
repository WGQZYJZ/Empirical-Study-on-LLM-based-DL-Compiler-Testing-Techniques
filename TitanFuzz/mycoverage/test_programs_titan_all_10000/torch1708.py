import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(4, 3)
result = torch.Tensor.narrow(input_tensor, 1, 1, 2)