import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(3, 3)
(sign, logdet) = torch.slogdet(input_data)