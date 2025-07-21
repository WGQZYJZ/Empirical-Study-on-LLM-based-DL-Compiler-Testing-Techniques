import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randint(0, 10, (1, 10))
index = torch.tensor([[4, 5, 6, 7], [3, 3, 3, 3]], dtype=torch.long)
src = torch.tensor([3, 4, 5, 6], dtype=torch.float)
output_tensor = torch.Tensor.scatter_add_(input_tensor, dim=0, index=index, src=src)