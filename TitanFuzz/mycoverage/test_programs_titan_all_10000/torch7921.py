import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.arange(1, 10, dtype=torch.float)
output_data = torch.exp2(input_data)