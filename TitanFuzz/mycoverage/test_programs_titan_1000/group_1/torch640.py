import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(5, 5)
result = torch.std(input_data)