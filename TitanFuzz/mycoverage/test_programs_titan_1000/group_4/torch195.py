import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randint(0, 100, (4, 4), dtype=torch.int32)
torch.Tensor.gcd_(input_tensor, torch.tensor(3))