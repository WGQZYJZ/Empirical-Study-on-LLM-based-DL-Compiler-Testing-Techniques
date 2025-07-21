import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([2, 3])
other_data = torch.tensor([4, 5])
output_data = torch.mul(input_data, other_data)