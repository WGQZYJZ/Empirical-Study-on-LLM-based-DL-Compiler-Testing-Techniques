import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 3)
index = torch.tensor([0, 2])
output_tensor = torch.Tensor.index_copy(input_tensor, dim=0, index=index, source=torch.tensor([[1, 1, 1], [2, 2, 2]]))