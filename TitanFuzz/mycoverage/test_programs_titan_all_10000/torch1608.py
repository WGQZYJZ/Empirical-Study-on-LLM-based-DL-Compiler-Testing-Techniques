import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 4)
index = torch.tensor([[0, 1], [1, 2]])
torch.gather(input, 0, index)
input = torch.randn(3, 4)
index = torch.tensor([[0, 1], [1, 2]])
torch.gather(input, 0, index)