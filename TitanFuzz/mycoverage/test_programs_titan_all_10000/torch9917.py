import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(4, 3)
other_tensor = torch.randn(3, 4)
result = torch.Tensor.view_as(input_tensor, other_tensor)