import torch
from torch import nn
from torch.autograd import Variable
x = torch.randint(low=0, high=10, size=(4, 4))
y = torch.randint(low=0, high=10, size=(4, 4), dtype=torch.float32)