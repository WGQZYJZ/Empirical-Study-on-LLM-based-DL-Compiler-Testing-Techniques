import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3, 5)
num_elements = torch.numel(input_data)