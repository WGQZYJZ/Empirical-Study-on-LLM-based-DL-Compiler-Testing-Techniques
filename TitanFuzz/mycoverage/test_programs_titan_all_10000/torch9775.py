import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(4, 3)
result_tensor = torch.Tensor.sort(input_tensor, dim=(- 1), descending=False)