import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330])
y = torch.sin(x)