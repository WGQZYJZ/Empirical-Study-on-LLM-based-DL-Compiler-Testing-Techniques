import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(10, 10)
result = torch.Tensor.corrcoef(input_tensor)