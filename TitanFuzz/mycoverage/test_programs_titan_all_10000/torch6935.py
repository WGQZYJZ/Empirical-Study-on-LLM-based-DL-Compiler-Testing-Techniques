import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.arange(0, 10, dtype=torch.float32)
result = torch.Tensor.floor_divide(input_tensor, 3)