import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, 2], [3, 4]])
other = torch.tensor([[1, 0], [1, 2]])
torch.Tensor.ne(input_tensor, other)