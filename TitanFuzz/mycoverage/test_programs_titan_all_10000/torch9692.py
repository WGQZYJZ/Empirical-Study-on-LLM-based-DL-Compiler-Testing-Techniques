import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(3, 3)
x = torch.randn(3, 3)
torch.nn.functional.threshold(x, 0.5, 0.0, inplace=True)
torch.nn.functional.threshold(x, 0.5, 0.0, inplace=False)