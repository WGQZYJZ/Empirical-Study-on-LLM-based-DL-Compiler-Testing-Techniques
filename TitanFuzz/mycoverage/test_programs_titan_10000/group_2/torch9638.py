import torch
from torch import nn
from torch.autograd import Variable

x = torch.randint(0, 10, (4, 5))
y = torch.rot90(x, 3, dims=(0, 1))