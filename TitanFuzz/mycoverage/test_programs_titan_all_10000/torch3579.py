import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[1, 1], [1, 0], [0, 1], [0, 0]], dtype=torch.float)
output = torch.logical_xor((input_data[:, 0] > 0), (input_data[:, 1] > 0))