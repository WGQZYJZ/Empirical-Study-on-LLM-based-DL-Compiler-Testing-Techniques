import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(3, 4)
mask = torch.tensor([[1, 1, 0, 0], [0, 0, 0, 1], [1, 0, 1, 0]], dtype=torch.uint8)
output_tensor = torch.Tensor.sparse_mask(_input_tensor, mask)