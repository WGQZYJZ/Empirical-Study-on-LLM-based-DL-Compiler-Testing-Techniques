import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3, 3)
result = torch.Tensor.logdet(input_tensor)