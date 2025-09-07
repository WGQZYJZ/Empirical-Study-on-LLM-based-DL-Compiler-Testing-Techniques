import torch
from torch import nn
from torch.autograd import Variable

x = torch.tensor([[1, 2, 3], [4, 5, 6]])
torch.chunk(x, 2, dim=1)