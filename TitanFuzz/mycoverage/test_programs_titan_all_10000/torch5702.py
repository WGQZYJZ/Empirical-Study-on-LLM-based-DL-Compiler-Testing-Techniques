import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3)
output_data = torch.nn.Softmin(dim=0)
output_data = torch.nn.Softmin(dim=1)
output_data = torch.nn.Softmin(dim=None)
output_data = torch.nn.Softmin(dim=(- 1))
output_data = torch.nn.Softmin(dim=(- 2))