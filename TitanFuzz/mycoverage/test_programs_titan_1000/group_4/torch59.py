import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3)
result = torch.special.expit(input_data)