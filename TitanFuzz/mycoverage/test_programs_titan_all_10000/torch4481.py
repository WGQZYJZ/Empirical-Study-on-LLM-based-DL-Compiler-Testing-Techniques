import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(2, 3)
output = torch.any((x > 0))
output = torch.any((x > 0), dim=0)
output = torch.any((x > 0), dim=1)
output = torch.any((x > 0), dim=1, keepdim=True)