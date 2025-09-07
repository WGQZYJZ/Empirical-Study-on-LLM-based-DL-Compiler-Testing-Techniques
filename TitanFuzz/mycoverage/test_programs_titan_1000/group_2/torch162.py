import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
exponent = 2
output_tensor = torch.Tensor.float_power_(input_tensor, exponent)