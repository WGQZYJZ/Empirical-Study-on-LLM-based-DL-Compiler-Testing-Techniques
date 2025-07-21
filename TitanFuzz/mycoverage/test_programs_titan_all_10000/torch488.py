import torch
from torch import nn
from torch.autograd import Variable
inputs = torch.tensor([[1.0, 2.0, 3.0, 4.0, 5.0], [1.0, 2.0, 3.0, 4.0, 5.0]])
output = torch.nansum(inputs, dim=1)