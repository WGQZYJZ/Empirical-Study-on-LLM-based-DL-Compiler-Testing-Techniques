import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
output = torch.full(input_data.size(), 3)