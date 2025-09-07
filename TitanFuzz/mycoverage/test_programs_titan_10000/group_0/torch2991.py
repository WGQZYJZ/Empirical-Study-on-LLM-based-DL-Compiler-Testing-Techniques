import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.rand(1, 3, 224, 224)
ignored_functions = torch.overrides.get_ignored_functions()