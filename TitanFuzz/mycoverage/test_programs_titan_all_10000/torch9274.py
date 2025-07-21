import torch
from torch import nn
from torch.autograd import Variable
tensor = torch.empty(2, 2)
torch.nn.init.uniform_(tensor, a=0.0, b=1.0)