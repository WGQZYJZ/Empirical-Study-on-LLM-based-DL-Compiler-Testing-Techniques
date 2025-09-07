import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.randn(5, 4)
output_data = torch.nn.functional.tanhshrink(input_data)