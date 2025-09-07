import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(1, 1, 10, 10, 10)
output = torch.nn.AdaptiveMaxPool3d((1, 1, 1))(input)
(output, indices) = torch.nn.AdaptiveMaxPool3d((1, 1, 1), return_indices=True)(input)