import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3)
other_tensor = torch.randn(2, 3)
result = torch.Tensor.add(input_tensor, other_tensor)