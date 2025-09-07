import torch
from torch import nn
from torch.autograd import Variable

x = torch.rand(1, 3, 4, 4)
out = torch.nn.functional.relu6(x)