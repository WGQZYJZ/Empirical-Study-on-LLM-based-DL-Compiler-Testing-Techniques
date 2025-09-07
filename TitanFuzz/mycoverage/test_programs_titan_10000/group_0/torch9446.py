import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.rand(1, 2, 3)
output_tensor = torch.log10(input_tensor)