import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.Tensor([[1, 2], [3, 4]])
torch.Tensor.neg_(input_tensor)