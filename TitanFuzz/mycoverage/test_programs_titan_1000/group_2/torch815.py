import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 3)
other_tensor = torch.randn(3, 3)
result = torch.greater(input_tensor, other_tensor)