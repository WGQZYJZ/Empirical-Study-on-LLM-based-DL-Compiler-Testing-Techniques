import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3)
output = torch.masked_select(input_data, torch.tensor([[0, 1, 0], [1, 1, 1]], dtype=torch.uint8))