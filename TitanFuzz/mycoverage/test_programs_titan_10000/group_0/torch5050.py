import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.Tensor([[1, 2], [3, 4]])
torch.Tensor.tanh_(input_tensor)