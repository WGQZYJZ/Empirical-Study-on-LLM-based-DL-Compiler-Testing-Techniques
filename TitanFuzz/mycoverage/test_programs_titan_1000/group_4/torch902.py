import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 3, 224, 224)
output_data = torch.Tensor.new_ones(input_data, (1, 3, 224, 224))