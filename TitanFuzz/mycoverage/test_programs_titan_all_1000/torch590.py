import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([1, 2, 3, 4, 5])
y = torch.tensor([4, 5, 6, 7, 8])
z = torch.greater(x, y)