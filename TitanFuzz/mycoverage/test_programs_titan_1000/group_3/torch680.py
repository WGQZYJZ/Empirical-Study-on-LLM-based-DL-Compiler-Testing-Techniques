import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[2, 3, 5], [4, 6, 8]])
other = torch.tensor([[1, 2, 3], [4, 5, 6]])
torch.Tensor.lcm_(input_tensor, other)