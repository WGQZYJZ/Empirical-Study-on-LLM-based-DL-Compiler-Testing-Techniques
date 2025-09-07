import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.randn(2, 3)
result = torch.Tensor.heaviside(input_tensor, values=0.5)