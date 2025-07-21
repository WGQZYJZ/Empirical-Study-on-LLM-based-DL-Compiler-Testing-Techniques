import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
other = torch.tensor([[7, 8, 9], [10, 11, 12]])
torch.Tensor.lcm_(input_tensor, other)