import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randint(0, 2, (2, 3, 3), dtype=torch.bool)
output_data = torch.Tensor.bitwise_and_(input_data, input_data)