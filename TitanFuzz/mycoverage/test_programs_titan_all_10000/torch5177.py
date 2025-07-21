import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 4)
torch._assert((input_data.dim() == 2), 'The input data is not 2D')
torch._assert((input_data.size(0) == 2), 'The first dimension is not 2')
torch._assert((input_data.size(1) == 4), 'The second dimension is not 4')