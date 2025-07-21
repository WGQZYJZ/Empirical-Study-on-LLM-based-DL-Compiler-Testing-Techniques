import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 4)
torch.Tensor.index_add_(input_tensor, 1, torch.tensor([0, 1, 2, 3]), torch.tensor([1, 2, 3, 4]))
torch.Tensor.index_add_(input_tensor, 1, torch.tensor([0, 1, 2, 3]), torch.tensor([1, 2, 3, 4]), alpha=0.5)