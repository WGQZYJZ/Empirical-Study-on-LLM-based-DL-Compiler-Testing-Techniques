import torch
from torch import nn
from torch.autograd import Variable
input_data = [torch.rand(2, 3), torch.rand(4, 3), torch.rand(4, 3)]
output = torch.block_diag(*input_data)