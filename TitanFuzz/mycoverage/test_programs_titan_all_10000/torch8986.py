import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=torch.float)
input_data_other = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=torch.float)
output_data = torch.dot(input_data, input_data_other)