import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(4, 3, 2)
output = torch.Tensor.storage_offset(input_tensor)