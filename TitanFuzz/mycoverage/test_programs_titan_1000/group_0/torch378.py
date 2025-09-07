import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
result = torch.eye(3, 3)