import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[1, 2], [3, 4]])
result = torch.prod(input_data, dim=1)