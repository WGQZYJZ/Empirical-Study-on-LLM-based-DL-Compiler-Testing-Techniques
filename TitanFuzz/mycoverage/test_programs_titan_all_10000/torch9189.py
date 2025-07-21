import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, 2], [3, 4]])
other = torch.tensor([[5, 6], [7, 8]])
torch.Tensor.sub_(input_tensor, other)