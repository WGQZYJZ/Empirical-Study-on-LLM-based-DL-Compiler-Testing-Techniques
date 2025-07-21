import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([[1, 2], [3, 4]])
y = torch.tensor([[5, 6]])
z = torch.broadcast_tensors(x, y)