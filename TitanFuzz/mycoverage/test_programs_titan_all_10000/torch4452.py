import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3, dtype=torch.float32)
output_data = torch.trunc(input_data)