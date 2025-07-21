import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randint(low=0, high=100, size=(3, 3), dtype=torch.float32)
other = torch.randint(low=0, high=100, size=(3, 3), dtype=torch.float32)
torch.Tensor.xlogy_(input_tensor, other)
input_tensor = torch.randint(low=0, high=100, size=(3, 3), dtype=torch.float32)
other = torch.randint