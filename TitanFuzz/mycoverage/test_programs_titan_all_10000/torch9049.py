import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([[1, 0, 0, 1, 1], [1, 1, 0, 0, 1]])
(unique_input, inverse_input, counts_input) = torch.unique(input, return_inverse=True, return_counts=True)