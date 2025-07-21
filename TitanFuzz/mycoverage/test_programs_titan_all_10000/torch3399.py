import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 1, 2, 2)
output = torch.is_conj(input_data)