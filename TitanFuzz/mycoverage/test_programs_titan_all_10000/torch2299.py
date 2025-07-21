import torch
from torch import nn
from torch.autograd import Variable
tensor = torch.randn(2, 3)
torch.nn.init.xavier_uniform_(tensor)