import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3)
divisor = torch.randn(3)
divisor = divisor.view(1, 3)
output_tensor = torch.true_divide(input_tensor, divisor)