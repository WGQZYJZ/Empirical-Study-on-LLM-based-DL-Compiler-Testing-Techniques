import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.arange(1, 10, dtype=torch.float32)
output_data = torch.randperm(input_data.size(0))