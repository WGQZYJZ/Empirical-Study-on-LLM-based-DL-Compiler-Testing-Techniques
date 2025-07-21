import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3)
output_data = torch.nn.functional.logsigmoid(input_data)
output_data = torch.sigmoid(input_data)
output_data = torch.log(output_data)
output_data = torch.log(input_data)