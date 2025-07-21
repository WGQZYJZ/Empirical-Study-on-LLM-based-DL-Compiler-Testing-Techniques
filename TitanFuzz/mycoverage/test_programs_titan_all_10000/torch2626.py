import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(2, 3, 4)
result = torch.Tensor.sort(input_tensor, dim=(- 1), descending=False)