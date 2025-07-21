import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.arange(10, dtype=torch.float32)
output_data = torch.clip(input_data, min=2, max=8)