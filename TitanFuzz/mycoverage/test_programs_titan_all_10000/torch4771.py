import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
other_tensor = torch.tensor([[7, 8, 9], [10, 11, 12], [13, 14, 15]])
torch.Tensor.expand_as(input_tensor, other_tensor)