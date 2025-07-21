import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(3, 5)
output_data = torch.is_conj(input_data)