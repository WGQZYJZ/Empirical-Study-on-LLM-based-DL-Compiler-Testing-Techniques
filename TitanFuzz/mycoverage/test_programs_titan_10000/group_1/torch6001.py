import torch
from torch import nn
from torch.autograd import Variable

data_input = torch.Tensor([[1, 2, 3], [4, 5, 6]])
torch.jit.isinstance(data_input, torch.Tensor)