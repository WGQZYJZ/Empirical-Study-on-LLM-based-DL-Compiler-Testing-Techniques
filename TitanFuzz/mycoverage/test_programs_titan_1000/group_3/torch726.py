import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(4, 3)
other = torch.randn(4, 3)
result = torch.Tensor.logaddexp2(input_tensor, other)