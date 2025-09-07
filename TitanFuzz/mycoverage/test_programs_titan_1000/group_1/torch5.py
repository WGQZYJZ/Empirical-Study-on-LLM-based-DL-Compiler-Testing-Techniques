import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[1, 2], [3, 4]])
output_data = torch.permute(input_data, (1, 0))