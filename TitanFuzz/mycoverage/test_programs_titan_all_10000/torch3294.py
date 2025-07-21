import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([True, False, True])
output_data = torch.logical_not(input_data)