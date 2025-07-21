import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3, 4, 5)
logdet = torch.Tensor.logdet(input_tensor)