import torch
from torch import nn
from torch.autograd import Variable
inp = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]])
out = torch.eye(inp.shape[1], inp.shape[0])