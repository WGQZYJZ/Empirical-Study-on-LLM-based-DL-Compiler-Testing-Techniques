import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3)
silu = torch.nn.SiLU(inplace=False)
output = silu(input_data)