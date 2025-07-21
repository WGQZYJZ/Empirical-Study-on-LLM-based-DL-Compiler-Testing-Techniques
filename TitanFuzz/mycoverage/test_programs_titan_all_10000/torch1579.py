import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(3, 3)
indices = torch.triu_indices(3, 3, offset=0, dtype=torch.long)