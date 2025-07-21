import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(2, 3)
torch.overrides.get_ignored_functions()