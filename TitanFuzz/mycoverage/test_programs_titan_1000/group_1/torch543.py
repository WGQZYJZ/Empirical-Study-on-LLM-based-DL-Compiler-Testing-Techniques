import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(10, 5)
output_data = torch.svd(input_data)