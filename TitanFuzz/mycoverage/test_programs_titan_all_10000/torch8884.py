import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[True, False], [False, True]], dtype=torch.bool)
output_data = torch.logical_not(input_data)