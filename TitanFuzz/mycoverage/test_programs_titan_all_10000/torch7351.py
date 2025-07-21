import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(2, 3)
result = torch.is_storage(input_data)