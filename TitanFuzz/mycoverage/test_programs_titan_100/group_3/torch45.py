import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=torch.int8)
other_data = torch.tensor([[1, 0, 1], [0, 1, 1], [1, 1, 1]], dtype=torch.int8)
result = torch.bitwise_and(input_data, other_data)