import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.randn(10, 3)
sorted_tensor = torch.Tensor.msort(input_tensor)