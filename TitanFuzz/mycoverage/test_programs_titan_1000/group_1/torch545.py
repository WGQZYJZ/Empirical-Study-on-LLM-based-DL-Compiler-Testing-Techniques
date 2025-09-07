import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3, 5)
atanh_result = torch.atanh(input_data)