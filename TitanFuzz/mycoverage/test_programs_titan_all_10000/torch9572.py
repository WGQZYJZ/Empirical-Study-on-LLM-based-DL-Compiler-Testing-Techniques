import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 5, dtype=torch.float)
pinv_input = torch.pinverse(input)