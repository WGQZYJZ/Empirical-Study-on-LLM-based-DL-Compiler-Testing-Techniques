import torch
from torch import nn
from torch.autograd import Variable
data = torch.randn(1, 2, 3, 4)
torch.nn.functional.celu(data)