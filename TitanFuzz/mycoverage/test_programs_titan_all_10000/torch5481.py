import torch
from torch import nn
from torch.autograd import Variable
x = torch.arange(0, 3, 1)
y = torch.arange(0, 3, 1)
(grid_x, grid_y) = torch.meshgrid(x, y)