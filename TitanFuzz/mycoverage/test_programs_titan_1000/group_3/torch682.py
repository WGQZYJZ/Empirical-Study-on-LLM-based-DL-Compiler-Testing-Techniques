import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
other = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
result = torch.Tensor.atan2_(input_tensor, other)