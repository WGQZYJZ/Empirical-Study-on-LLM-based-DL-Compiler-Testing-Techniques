import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(1, 3, 4, 5)
torch.Tensor.erfinv(input_tensor)