import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 3, dtype=torch.float)
mask = torch.tensor([[1, 0, 1], [0, 1, 0], [1, 0, 1]], dtype=torch.uint8)
tensor = torch.tensor([1, 2, 3], dtype=torch.float)
output_tensor = torch.Tensor.masked_scatter(input_tensor, mask, tensor)