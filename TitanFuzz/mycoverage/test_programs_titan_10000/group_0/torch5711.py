import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.randn(4, 4, dtype=torch.float)
output_data = torch.conj_physical(input_data)