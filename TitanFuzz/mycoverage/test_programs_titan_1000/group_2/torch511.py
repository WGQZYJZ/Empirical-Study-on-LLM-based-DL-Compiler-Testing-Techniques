import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, 2, 3, 3, 3, 3, 1, 2, 3, 3, 3, 3], [1, 2, 3, 3, 3, 3, 1, 2, 3, 3, 3, 3]])
result = torch.Tensor.unique_consecutive(input_tensor, return_inverse=False, return_counts=False, dim=None)