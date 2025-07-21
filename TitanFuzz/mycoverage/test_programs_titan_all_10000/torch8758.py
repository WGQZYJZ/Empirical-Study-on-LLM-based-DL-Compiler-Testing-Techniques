import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.arange(0, 10, dtype=torch.float)
output_data = torch.full_like(input_data, fill_value=3.14, dtype=torch.float)