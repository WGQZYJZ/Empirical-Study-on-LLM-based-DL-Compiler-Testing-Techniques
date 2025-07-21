import torch
from torch import nn
from torch.autograd import Variable
data = torch.randn(3, 4)
torch.overrides.get_ignored_functions()