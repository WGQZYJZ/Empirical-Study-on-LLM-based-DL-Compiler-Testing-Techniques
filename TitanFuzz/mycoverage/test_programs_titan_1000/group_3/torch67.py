import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([1, 3, 2, 3, 4, 2])
(unique_data, inverse_data, counts_data) = torch.unique(input_data, sorted=True, return_inverse=True, return_counts=True, dim=None)