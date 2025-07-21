import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([1, 2])
y = torch.tensor([3, 4])
z = torch.stack([x, y])