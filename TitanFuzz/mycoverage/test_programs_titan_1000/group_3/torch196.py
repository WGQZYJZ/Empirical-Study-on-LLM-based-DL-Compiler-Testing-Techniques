import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3)
(max_val, max_idx) = torch.amax(input_data, 1)