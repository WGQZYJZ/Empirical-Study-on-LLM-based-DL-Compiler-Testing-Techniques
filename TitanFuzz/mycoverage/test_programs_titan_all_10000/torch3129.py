import torch
from torch import nn
from torch.autograd import Variable
tensor = torch.empty(3, 3)
torch.nn.init.xavier_normal_(tensor)