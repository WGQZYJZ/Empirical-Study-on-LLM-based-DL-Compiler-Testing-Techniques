import torch
from torch import nn
from torch.autograd import Variable
data = torch.randn(3, 5)
result = torch.nn.functional.hardtanh(data)