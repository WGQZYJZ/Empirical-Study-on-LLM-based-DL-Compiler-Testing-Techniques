import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(2, 3, 4)
output_data = torch.einsum('ijk,ijl->ikl', input_data, input_data)
input_data = torch.rand(2, 3, 4)
output_data = torch.einsum('ijk,ijl->ikl', input_data, input_data)