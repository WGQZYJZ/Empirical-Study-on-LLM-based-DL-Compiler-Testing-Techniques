import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, 2], [3, 4]])
other = torch.tensor([[1, 2], [3, 4]])
result = torch.Tensor.equal(input_tensor, other)