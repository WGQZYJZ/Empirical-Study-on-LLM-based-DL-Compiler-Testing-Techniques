import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(4, 4)
torch.nn.functional.tanhshrink(input_data)
input_data = torch.randn(4, 4)
torch.nn.functional.threshold(input_data, 0.5, 0.6)