import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(2, 3, 3)
torch.as_strided(input_data, (3, 2, 2), (1, 3, 3))
torch.as_strided(input_data, (2, 3, 3), (1, 1, 1))
torch.as_strided(input_data, (2, 3, 3), (1, 3, 3))
torch.as_strided(input_data, (3, 2, 2), (1, 1, 1))
torch.as_strided(input_data, (3, 2, 2), (1, 1, 1), 1)