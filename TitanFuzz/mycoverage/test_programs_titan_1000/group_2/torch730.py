import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
other = torch.tensor([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
bitwise_or = torch.Tensor.bitwise_or(input_tensor, other)