import torch
from torch import nn
from torch.autograd import Variable

tensor = torch.empty(2, 3)
torch.nn.init.zeros_(tensor)
tensor = torch.empty(2, 3)
torch.nn.init.ones_(tensor)
tensor = torch.empty(2, 3)