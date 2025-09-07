import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3)
output_data = torch.nn.functional.softmin(input_data, dim=1)
output_data = torch.nn.functional.softmin(input_data, dim=0)
output_data = torch.nn.functional.softmin(input_data, dim=None)