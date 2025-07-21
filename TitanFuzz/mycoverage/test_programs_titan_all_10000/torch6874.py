import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 3)
index_tensor = torch.tensor([0, 2, 1])
update_tensor = torch.tensor([1, 2, 3])
output_tensor = torch.Tensor.index_add_(input_tensor, 0, index_tensor, update_tensor)