import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.Tensor([[1, 0], [0, 1]])
output_tensor = torch.Tensor.bitwise_not(input_tensor)