import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3)
other_data = torch.randn(2, 3)
output_data = torch.less(input_data, other_data)