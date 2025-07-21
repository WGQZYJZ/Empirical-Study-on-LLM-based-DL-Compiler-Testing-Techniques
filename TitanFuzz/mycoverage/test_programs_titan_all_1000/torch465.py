import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(3, 4)
output_data = torch.scatter(input_data, 1, torch.tensor([[2], [0], [1]]), 0.5)
input_data = torch.randn(3, 4)