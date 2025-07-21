import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(2, 3)
output_data = torch.full_like(input_data, fill_value=3)