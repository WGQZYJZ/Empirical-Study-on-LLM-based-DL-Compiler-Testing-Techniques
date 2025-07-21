import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(5, 3)
identity = torch.nn.Identity()
output = identity(input_data)