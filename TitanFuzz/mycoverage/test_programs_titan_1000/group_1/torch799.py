import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3, 4, 5)
output = torch.is_complex(input_data)