import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
other = torch.tensor([[0, 0, 0], [6, 5, 4]])
torch.Tensor.less_equal_(input_tensor, other)