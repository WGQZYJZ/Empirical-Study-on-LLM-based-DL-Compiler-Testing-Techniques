import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.rand(1, 3, 3)
result_tensor = torch.Tensor.erf(input_tensor)