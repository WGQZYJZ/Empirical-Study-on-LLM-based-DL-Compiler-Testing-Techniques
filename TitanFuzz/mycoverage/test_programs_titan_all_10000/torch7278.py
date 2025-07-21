import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(4, 4)
other_tensor = torch.randn(4, 4)
result = torch.ge(input_tensor, other_tensor)