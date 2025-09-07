import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3)
resize_as_tensor = torch.randn(2, 3)
torch.Tensor.resize_as_(input_tensor, resize_as_tensor)