import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.int32)
other = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.int32)
torch.Tensor.gcd_(input_tensor, other)