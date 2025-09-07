import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.arange(1, 10, dtype=torch.float32)
result = torch.floor_divide(input_tensor, 2)