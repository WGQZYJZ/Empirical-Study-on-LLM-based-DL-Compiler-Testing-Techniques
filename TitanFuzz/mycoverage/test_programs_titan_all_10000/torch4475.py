import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(3, 3)
triu_indices = torch.triu_indices(3, 3, offset=1)