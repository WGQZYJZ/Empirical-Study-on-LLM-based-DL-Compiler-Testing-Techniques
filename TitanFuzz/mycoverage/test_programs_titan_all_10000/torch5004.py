import torch
from torch import nn
from torch.autograd import Variable
x = (torch.randn(100, 1) * 10)
y = (x + (torch.randn(100, 1) * 3))
torch.utils.data.TensorDataset(x, y)
x = (torch.randn(100, 1) * 10)
y = (x + (torch.randn(100, 1) * 3))
torch.utils.data.TensorDataset(x, y)