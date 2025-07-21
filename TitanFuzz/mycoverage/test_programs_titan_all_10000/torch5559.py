import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([2, 3, 4, 5])
output_data = torch.square(input_data)
input_data = torch.tensor([4, 9, 16, 25])
output_data = torch.sqrt(input_data)