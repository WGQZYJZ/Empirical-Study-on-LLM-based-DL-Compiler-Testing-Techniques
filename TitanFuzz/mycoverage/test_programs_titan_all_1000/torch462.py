import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(2, 3)
result = torch.Tensor.erfc(input_tensor)