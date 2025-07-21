import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([1, 2, 3, 4])
y = torch.unsqueeze(x, 0)
y = torch.unsqueeze(x, 1)