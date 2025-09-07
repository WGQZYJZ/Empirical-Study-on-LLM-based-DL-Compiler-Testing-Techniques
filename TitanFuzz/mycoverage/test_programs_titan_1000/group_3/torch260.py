import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=torch.bool)
other_data = torch.tensor([[1, 1, 0], [1, 0, 1], [0, 1, 1]], dtype=torch.bool)
output = torch.bitwise_xor(input_data, other_data)