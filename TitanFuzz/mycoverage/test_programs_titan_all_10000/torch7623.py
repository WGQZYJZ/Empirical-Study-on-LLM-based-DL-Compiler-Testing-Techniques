import torch
from torch import nn
from torch.autograd import Variable
x = torch.Tensor([1, 2, 3])
y = torch.Tensor([1, 1, 1])
result = torch.broadcast_tensors(x, y)