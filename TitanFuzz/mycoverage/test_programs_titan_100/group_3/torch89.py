import torch
from torch import nn
from torch.autograd import Variable
size_tensor = torch.Size([2, 3])
fill_value = 0.1
output_tensor = torch.full(size_tensor, fill_value)