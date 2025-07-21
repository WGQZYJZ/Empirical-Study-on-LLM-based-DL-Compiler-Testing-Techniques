import torch
from torch import nn
from torch.autograd import Variable
input_data = [torch.rand(1, 2), torch.rand(1, 2)]
output_data = torch.column_stack(input_data)