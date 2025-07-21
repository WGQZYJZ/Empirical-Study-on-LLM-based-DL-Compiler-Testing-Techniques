import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[1, 1, 1], [1, 1, 0], [1, 0, 1], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 0, 1], [0, 0, 0]], dtype=torch.bool)
other_data = torch.tensor([[1, 1, 1], [1, 1, 0], [1, 0, 1], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 0, 1], [0, 0, 0]], dtype=torch.bool)
output_data = torch.logical_or(input_data, other_data)