import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.arange(0, 6)
output_data = torch.as_strided(input_data, (3, 2), (2, 1))
input_data = torch.arange(0, 6)
output_data = torch.as_strided(input_data, (3, 2), (2, 1))