import torch
from torch import nn
from torch.autograd import Variable
input_data_1 = torch.rand(3, 1)
input_data_2 = torch.rand(3, 1)
output_data = torch.column_stack((input_data_1, input_data_2))