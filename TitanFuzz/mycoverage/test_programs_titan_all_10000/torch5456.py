import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(1, 1, 32, 32)
torch.overrides.wrap_torch_function(torch.nn.functional.conv2d)
torch.overrides.wrap_torch_function(torch.nn.functional.conv2d)
torch.overrides.wrap_torch_function(torch.nn.functional.conv2d)