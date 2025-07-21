import torch
from torch import nn
from torch.autograd import Variable
input_data = [torch.randn(1, 3), torch.randn(2, 3)]
vector = torch.nn.utils.parameters_to_vector(input_data)