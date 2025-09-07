import torch
from torch import nn
from torch.autograd import Variable
input = torch.randint(10, (2, 3), dtype=torch.int32)
output = torch.full_like(input, fill_value=0, dtype=torch.float32)