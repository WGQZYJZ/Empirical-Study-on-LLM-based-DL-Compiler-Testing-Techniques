import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 3, 224, 224)
mish = torch.nn.functional.mish(input)