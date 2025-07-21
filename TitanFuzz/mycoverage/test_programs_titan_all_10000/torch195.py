import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3)
log_softmax = torch.nn.functional.log_softmax(input, dim=1)