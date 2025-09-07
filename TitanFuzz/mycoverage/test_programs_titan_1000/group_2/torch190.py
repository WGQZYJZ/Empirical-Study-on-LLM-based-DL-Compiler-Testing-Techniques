import torch
from torch import nn
from torch.autograd import Variable
input_data = (torch.rand(3, 4), torch.rand(3, 4))
output_data = torch.column_stack(input_data)