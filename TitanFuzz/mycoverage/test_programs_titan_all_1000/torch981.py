import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[1, 2, 3], [4, 5, 6]])
other_data = torch.tensor([[1, 1, 1], [1, 1, 1]])
result = torch.ne(input_data, other_data)