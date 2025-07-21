import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float32)
index = torch.tensor([0, 2, 1, 0], dtype=torch.int64)
src = torch.tensor([[10, 20, 30], [40, 50, 60], [70, 80, 90], [100, 200, 300]], dtype=torch.float32)
dim = 0
output_tensor = torch.Tensor.scatter_add(input_tensor, dim, index, src)