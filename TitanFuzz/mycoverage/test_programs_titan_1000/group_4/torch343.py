import torch
from torch import nn
from torch.autograd import Variable
input_data = [torch.randn(2, 3), torch.randn(2, 3), torch.randn(2, 3)]
output_data = torch.column_stack(input_data)