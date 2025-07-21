import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[0, 1, 0, 1], [1, 0, 1, 0], [1, 0, 1, 0], [0, 1, 0, 1]])
other = torch.tensor([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]])
torch.Tensor.bitwise_xor_(input_tensor, other)