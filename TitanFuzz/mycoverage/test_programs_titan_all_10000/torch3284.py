import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([4, 5, 6, 7, 8, 9])
output_data = torch.tile(input_data, (2,))