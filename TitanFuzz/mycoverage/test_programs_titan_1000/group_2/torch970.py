import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3)
result = torch.special.polygamma(1, input_tensor)