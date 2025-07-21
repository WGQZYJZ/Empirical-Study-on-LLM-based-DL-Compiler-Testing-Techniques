import torch
from torch import nn
from torch.autograd import Variable
data = torch.randn(2, 3)
torch.set_warn_always(True)
data.add(1)