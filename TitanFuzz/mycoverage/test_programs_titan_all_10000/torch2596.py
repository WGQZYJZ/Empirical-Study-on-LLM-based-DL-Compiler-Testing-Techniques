import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 1, 6, 6, 6)
output = torch.nn.functional.adaptive_max_pool3d(input, output_size=(2, 2, 2))