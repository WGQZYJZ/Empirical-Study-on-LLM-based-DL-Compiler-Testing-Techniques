import torch
from torch import nn
from torch.autograd import Variable
tensor = torch.empty(3, 3)
torch.nn.init.normal_(tensor, mean=0.0, std=1.0)