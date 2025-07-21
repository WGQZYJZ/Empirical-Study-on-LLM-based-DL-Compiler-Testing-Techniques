import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
y = torch.tensor([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
torch.where((x > 5), x, y)
torch.where((x > 5), x, y)
x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])