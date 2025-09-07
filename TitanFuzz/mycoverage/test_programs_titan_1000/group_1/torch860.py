import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 1, 2, 2)
torch.get_default_dtype()
input_data = input_data.type(torch.float64)