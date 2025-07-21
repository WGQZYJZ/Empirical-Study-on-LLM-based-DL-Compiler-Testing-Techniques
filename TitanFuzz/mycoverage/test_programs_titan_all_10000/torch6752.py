import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 5)
torch.nn.functional.threshold(input, 0.5, (- 0.5))