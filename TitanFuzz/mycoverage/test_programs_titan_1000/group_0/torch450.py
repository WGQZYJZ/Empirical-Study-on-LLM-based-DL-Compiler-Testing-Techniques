import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 1)
torch.nn.functional.logsigmoid(input)
input = torch.randn(1, 1)
torch.nn.functional.logsigmoid(input)