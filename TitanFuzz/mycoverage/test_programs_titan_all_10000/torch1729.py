import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 1, 5, 5)
output_size = (3, 3)
output = torch.nn.functional.adaptive_max_pool2d(input_data, output_size)