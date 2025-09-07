import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.randint(10, (2, 3), dtype=torch.float)
torch.Tensor.log1p_(input_tensor)