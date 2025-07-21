import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(100, 3)
y = torch.randn(100, 2)
dataset = torch.utils.data.TensorDataset(x, y)