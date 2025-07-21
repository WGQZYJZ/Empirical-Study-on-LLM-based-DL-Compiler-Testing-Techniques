import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randint(low=0, high=2, size=(1, 5), dtype=torch.uint8)
output_data = torch.Tensor.bitwise_not_(input_data)