import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.tensor([[0, 1, 2], [3, 4, 5]])
other = torch.tensor([[0, 0, 0], [3, 4, 5]])
result = torch.Tensor.less_equal_(input_tensor, other)