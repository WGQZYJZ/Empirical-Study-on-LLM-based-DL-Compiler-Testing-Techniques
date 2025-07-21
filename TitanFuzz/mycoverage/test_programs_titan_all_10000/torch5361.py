import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[1, 2, 3, 3, 3, 3, 3, 4], [1, 2, 3, 4, 4, 4, 4, 4]])
output_data = torch.unique_consecutive(input_data, return_inverse=True, return_counts=True)