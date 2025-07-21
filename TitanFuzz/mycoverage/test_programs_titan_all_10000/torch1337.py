import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(2, 3)
torch.nn.functional.relu(x)
torch.nn.functional.relu_(x)
x = torch.randn(2, 3)
torch.nn.functional.relu6(x)