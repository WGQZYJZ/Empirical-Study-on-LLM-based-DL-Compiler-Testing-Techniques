import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.randint(1, 100, (5, 5), dtype=torch.float32)
torch.Tensor.log2_(input_tensor)