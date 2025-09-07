import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.tensor([[0, 1], [1, 0]])
other = torch.tensor([[0, 1], [1, 0]])
result = torch.Tensor.not_equal_(input_tensor, other)