import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 4)
result = torch.Tensor.select(input_tensor, dim=0, index=2)