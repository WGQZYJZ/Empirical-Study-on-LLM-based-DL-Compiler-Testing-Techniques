import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(2, 3, 3, dtype=torch.float64)
(s, logdet) = torch.slogdet(input)