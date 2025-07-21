import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(3, 3)
torch._assert((input_data.dim() == 2), 'input_data.dim() must be 2')