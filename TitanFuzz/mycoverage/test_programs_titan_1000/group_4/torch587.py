import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(1, 1, 5))
output = torch.nn.functional.adaptive_max_pool1d(input, output_size=1)
output = torch.nn.functional.adaptive_max_pool1d(input, output_size=2)
output = torch.nn.functional.adaptive_max_pool1d(input, output_size=3)
output = torch.nn.functional.adaptive_max_pool1d(input, output_size=4)
output = torch.nn.functional.adaptive_max_pool1d(input, output_size=5)