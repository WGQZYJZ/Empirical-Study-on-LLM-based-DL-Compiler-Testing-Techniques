import torch
from torch import nn
from torch.autograd import Variable
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.normal_\ntorch.Tensor.normal_(_input_tensor, mean=0, std=1, *, generator=None)\n'
input_data = torch.randn(1, 3)
output_data = torch.Tensor.normal_(input_data, mean=0, std=1)