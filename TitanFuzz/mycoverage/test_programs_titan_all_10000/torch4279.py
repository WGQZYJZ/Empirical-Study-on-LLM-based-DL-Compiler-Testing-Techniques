import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 4)
mask = torch.tensor([0, 0, 1], dtype=torch.bool)
output_tensor = torch.Tensor.sparse_mask(input_tensor, mask)