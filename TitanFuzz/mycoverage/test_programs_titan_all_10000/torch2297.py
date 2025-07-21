import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], dtype=torch.float32)
input_data = input_data.reshape([1, 1, 10])
weight = torch.tensor([[1, 1, 1]], dtype=torch.float32)
weight = weight.reshape([1, 1, 3])
output = torch.nn.functional.conv_transpose1d(input_data, weight)