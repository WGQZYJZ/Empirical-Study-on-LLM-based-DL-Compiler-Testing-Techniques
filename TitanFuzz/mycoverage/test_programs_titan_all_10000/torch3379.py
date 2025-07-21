import torch
from torch import nn
from torch.autograd import Variable
input = torch.randint(0, 10, (2, 3), dtype=torch.float32)
torch.randint_like(input, low=0, high=10)