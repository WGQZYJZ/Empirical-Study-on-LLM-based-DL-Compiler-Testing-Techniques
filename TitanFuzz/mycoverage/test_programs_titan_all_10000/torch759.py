import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(5, 3)
result = torch.empty(5, 3)
torch.add(input_data, input_data, out=result)
input_data = torch.rand(5, 3)
result = torch.empty(5, 3)
torch.add(input_data, input_data, out=result)