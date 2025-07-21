import torch
from torch import nn
from torch.autograd import Variable
input_tensor = Variable(torch.randn(1, 3, 10, 10, 10))
output = torch.nn.functional.adaptive_max_pool3d(input_tensor, (1, 1, 1))
output = torch.nn.functional.adaptive_max_pool3d(input_tensor, (2, 2, 2))
output = torch.nn.functional.adaptive_max_pool3d(input_tensor, (4, 4, 4))