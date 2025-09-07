import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.randint(low=1, high=10, size=(5, 5), dtype=torch.int32)
torch.Tensor.gcd_(input_tensor, 3)