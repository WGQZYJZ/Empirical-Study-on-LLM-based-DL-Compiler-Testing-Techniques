import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.bool)
output_data = torch.logical_not(input_data)