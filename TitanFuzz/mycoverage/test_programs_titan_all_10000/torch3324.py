import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(3, 4)
softmin_result = torch.nn.functional.softmin(input_data, dim=1)