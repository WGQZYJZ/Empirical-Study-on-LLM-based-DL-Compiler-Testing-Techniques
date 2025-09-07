import torch
from torch import nn
from torch.autograd import Variable

tensor = torch.FloatTensor(3, 3)
torch.nn.init.zeros_(tensor)