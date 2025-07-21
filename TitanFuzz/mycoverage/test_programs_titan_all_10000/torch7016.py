import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 2)
inverse_tensor = torch.Tensor.inverse(input_tensor)