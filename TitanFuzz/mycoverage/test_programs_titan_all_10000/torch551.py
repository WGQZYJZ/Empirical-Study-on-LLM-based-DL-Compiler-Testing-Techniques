import torch
from torch import nn
from torch.autograd import Variable
data = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
result = torch.isposinf(data)