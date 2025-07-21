import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[1, 0, 0], [0, 1, 0], [1, 1, 1]], dtype=torch.bool)
output = torch.logical_not(input_data)