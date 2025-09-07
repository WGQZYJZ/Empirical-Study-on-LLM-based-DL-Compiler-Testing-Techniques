import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.randint(low=0, high=10, size=(3, 3), dtype=torch.float32)
result = torch.Tensor.cumprod_(input_tensor, dim=1)