import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([1, 2, 3, 5])
y = torch.vander(x, 2, True)
y = torch.vander(x, 3, True)
y = torch.vander(x, 4, True)
y = torch.vander(x, 5, True)