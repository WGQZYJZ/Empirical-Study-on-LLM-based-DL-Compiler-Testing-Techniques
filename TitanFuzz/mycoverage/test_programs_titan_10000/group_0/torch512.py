import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.arange(9, dtype=torch.float)
output_data = torch.diag(input_data)