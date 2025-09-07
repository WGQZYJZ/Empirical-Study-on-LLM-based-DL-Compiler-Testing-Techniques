import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4], [5, 5, 5, 5, 5], [6, 6, 6, 6, 6]], dtype=torch.float32)
nanmean_tensor = torch.Tensor.nanmean(input_tensor, dim=0, keepdim=False)