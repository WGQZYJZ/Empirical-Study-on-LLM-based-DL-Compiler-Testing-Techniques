import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(4, 4)
output = torch.Tensor.isinf(input_tensor)