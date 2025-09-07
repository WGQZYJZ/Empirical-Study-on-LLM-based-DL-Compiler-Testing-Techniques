import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 2, 3)
output_data = torch.atleast_3d(input_data)
output_data = torch.atleast_3d(input_data, input_data)
output_data = torch.atleast_3d(input_data, input_data, input_data)
output_data = torch.atleast_3d(input_data, input_data, input_data, input_data)