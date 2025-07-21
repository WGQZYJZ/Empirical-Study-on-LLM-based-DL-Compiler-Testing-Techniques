import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 8, 8, 9, 9, 9, 10, 10])
input_data = input_data.unsqueeze(0)
output_data = torch.unique_consecutive(input_data)