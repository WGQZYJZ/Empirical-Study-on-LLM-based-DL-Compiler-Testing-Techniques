import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3, 4)
output = torch.reshape(input_data, ((- 1), 6))