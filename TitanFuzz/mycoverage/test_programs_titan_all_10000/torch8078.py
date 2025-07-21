import torch
from torch import nn
from torch.autograd import Variable
img = torch.randn(1, 1, 4, 4)
out = torch.nn.MaxPool2d(2, 2, 0, 1, False, False)
out = out(img)