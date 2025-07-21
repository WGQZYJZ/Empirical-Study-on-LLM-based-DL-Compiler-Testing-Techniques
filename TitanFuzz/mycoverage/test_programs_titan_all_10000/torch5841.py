import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, 1, 1], [1, 1, 1]])
other = torch.tensor([[1, 1, 1], [1, 1, 1]])
torch.Tensor.cross(input_tensor, other, dim=(- 1))