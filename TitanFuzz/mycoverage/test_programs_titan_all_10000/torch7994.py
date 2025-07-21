import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[1, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3], [1, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]])
torch.unique_consecutive(input_data, return_inverse=False, return_counts=False, dim=None)