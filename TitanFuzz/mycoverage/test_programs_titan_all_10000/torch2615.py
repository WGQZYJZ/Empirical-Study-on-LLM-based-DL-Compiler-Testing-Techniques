import torch
from torch import nn
from torch.autograd import Variable
input1 = torch.randn(2, 3)
input2 = torch.randn(2, 3)
max_value = torch.maximum(input1, input2)