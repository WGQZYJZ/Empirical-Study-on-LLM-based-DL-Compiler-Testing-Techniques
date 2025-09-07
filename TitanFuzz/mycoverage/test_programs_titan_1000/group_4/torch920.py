import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
other_data = torch.tensor([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
result = torch.eq(input_data, other_data)