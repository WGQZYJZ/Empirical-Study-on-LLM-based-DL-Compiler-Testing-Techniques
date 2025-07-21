import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(20, dtype=torch.float32)
result_tensor = torch.Tensor.float_power_(input_tensor, exponent=2)