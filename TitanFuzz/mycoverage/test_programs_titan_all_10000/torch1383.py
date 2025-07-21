import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(5, 5)
_index = torch.tensor([[4, 3, 1], [3, 2, 0]])
_src = torch.tensor([[1, 0, 1], [1, 1, 0]], dtype=torch.float)
output = torch.Tensor.scatter_add(_input_tensor, dim=1, index=_index, src=_src)