import torch
from torch import nn
from torch.autograd import Variable
tensor = torch.empty(3, 3)
torch.nn.init.xavier_uniform_(tensor, gain=1.0)
tensor = torch.empty(3, 3)
torch.nn.init.xavier_normal_(tensor, gain=1.0)