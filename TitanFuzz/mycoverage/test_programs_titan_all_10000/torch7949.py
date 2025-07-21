import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.arange(1, 10, dtype=torch.float)
other_data = torch.arange(1, 10, dtype=torch.float)
output = torch.ldexp(input_data, other_data)