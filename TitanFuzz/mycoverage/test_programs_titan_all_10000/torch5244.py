import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 1, 3, 3)
torch.overrides.get_ignored_functions()