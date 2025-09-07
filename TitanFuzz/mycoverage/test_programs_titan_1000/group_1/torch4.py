import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([1, 2, 3])
torch.overrides.has_torch_function(x)