import torch
from torch import nn
from torch.autograd import Variable
batch_size = 3
input_size = 3
output_size = 3
input_data = torch.randn(batch_size, input_size, requires_grad=True)
output_data = torch.linalg.inv(input_data)