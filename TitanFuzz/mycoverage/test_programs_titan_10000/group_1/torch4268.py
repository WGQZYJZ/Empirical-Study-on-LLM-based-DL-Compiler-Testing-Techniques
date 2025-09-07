import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.randn(10, 10)
other_tensor = torch.randn(10, 10)
result = torch.logaddexp2(input_tensor, other_tensor)