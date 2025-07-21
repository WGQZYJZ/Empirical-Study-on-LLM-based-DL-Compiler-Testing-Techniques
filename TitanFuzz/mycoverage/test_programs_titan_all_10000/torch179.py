import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]])
output_data = torch.unsqueeze(input_data, dim=1)