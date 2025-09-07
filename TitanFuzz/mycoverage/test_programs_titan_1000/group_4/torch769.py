import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
other = torch.tensor([[1, 1, 1], [1, 1, 1]], dtype=torch.float32)
torch.Tensor.add_(input_tensor, other)