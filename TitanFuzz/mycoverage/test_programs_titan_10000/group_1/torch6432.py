import torch
from torch import nn
from torch.autograd import Variable

tensor = torch.zeros(2, 3)
torch.nn.init.constant_(tensor, 3.14)