import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3)
is_leaf = torch.Tensor.is_leaf(input_tensor)