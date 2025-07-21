import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(10, 2)
torch.overrides.has_torch_function(input_data)