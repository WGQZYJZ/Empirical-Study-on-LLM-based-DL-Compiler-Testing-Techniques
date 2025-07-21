import torch
from torch import nn
from torch.autograd import Variable
x = torch.arange(0, 4, 1)
y = torch.arange(0, 4, 1)
(x_mesh, y_mesh) = torch.meshgrid(x, y)
x = torch.arange(0, 4, 1)
y = torch.arange(0, 4, 1)
z = torch.arange(0, 4, 1)
(x_mesh, y_mesh, z_mesh) = torch.meshgrid(x, y, z)