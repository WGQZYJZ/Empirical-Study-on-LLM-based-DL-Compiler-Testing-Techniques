import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
other_data = torch.Tensor([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
output_data = torch.maximum(input_data, other_data)