import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([0, 30, 45, 60, 90])
y = torch.cos(x.float())