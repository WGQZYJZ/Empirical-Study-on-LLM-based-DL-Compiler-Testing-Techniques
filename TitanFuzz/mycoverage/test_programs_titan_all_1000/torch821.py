import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, 0, 0], [1, 1, 0]])
other = torch.tensor([[1, 0, 0], [1, 1, 0]])
output_tensor = torch.Tensor.bitwise_or_(input_tensor, other)