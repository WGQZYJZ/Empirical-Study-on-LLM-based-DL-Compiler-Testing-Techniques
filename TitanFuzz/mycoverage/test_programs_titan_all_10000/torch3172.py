import torch
from torch import nn
from torch.autograd import Variable
a = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = torch.rot90(a, 1, [0, 1])
b = torch.rot90(a, 2, [0, 1])
b = torch.rot90(a, 3, [0, 1])