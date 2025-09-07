import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.randn((2, 3))
logit_data = torch.special.logit(input_data)