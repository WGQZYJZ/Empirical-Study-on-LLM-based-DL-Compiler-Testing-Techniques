import torch
from torch import nn
from torch.autograd import Variable
x = torch.arange(0, 5)
y = torch.arange(0, 5)
(x_mesh, y_mesh) = torch.meshgrid(x, y)