import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(3, 3)
torch.set_warn_always(True)
torch.set_warn_always(False)