import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 1, 2, 2)
output_data = torch.nn.functional.hardtanh_(input_data)
output_data = torch.nn.functional.hardtanh_(input_data, min_val=0.5, max_val=1.5)