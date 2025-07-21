import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]])
y = torch.reshape(x, (2, 6))