import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(1, dtype=torch.float32)
other_data = torch.rand(1, dtype=torch.float32)
out = torch.logaddexp2(input_data, other_data)