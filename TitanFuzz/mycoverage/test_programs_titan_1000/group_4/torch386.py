import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.arange(1, 6, dtype=torch.float32)
output_data = torch.Tensor.lgamma(input_data)