import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3)
output_data = torch.reshape(input_data, ((- 1), 3))
output_data = torch.reshape(input_data, (3, (- 1)))
output_data = torch.reshape(input_data, (1, 6))
output_data = torch.reshape(input_data, (6, 1))
output_data = torch.reshape(input_data, (6,))
output_data = input_data.view((- 1), 3)
output_data = input