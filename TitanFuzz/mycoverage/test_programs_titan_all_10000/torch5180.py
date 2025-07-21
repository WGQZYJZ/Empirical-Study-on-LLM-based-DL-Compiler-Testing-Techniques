import torch
from torch import nn
from torch.autograd import Variable
tensor = torch.Tensor(3, 3)
torch.nn.init.eye_(tensor)