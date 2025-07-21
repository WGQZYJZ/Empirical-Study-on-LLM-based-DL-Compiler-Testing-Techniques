import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(5, 3)
index = torch.tensor([[4, 5, 4, 1], [3, 3, 1, 2]], dtype=torch.long)
src = torch.tensor([[1, 0.1, 1, 0.1], [2, 2, 2, 2]], dtype=torch.float)
output_tensor = torch.Tensor.scatter_add(input_tensor, dim=0, index=index, src=src)