import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
y = torch.tensor([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
torch.where((x > 4), x, y)
x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
y = torch.tensor([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
torch.where((x > 4), x, y)