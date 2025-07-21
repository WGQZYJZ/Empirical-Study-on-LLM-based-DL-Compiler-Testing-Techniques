import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 1, 3, 3)
output = torch.nn.functional.adaptive_max_pool2d(input, (1, 1))
(output, indices) = torch.nn.functional.adaptive_max_pool2d(input, (1, 1), return_indices=True)
output = torch.nn.functional.adaptive_max_pool2d(input, (3, 3))