import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(1, 3, 5)
result = torch.Tensor.argmax(input_tensor, dim=1, keepdim=True)