import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.arange(0, 180, dtype=torch.float)
output_data = torch.deg2rad(input_data)