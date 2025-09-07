import torch
from torch import nn
from torch.autograd import Variable

x = torch.tensor([(- 1), 0, 1])
torch.clip(x, min=(- 0.5), max=0.5)