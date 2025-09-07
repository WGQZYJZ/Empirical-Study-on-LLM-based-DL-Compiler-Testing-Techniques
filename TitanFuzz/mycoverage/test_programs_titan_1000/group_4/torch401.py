import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 2, 3)
is_complex = torch.is_complex(input_data)