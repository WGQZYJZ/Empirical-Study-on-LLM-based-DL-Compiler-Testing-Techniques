import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.Tensor([1, (- 1), 0.5])
torch.Tensor.acos_(input_tensor)