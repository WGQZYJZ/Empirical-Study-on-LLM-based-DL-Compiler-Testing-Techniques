import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(5, 10)
y = torch.nn.functional.logsigmoid(x)