import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(3, 5)
y = torch.nn.functional.relu6(x)