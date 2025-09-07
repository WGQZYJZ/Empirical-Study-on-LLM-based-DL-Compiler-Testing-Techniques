import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(3, 3)
result = torch.div(input_data, 2)
torch.add(input_data, 2, out=result)
result.add_(input_data)
result = torch.mul(input_data, input_data)
result.mul_(input_data)
result = torch.pow(input_data, 2)
result.pow_(2)