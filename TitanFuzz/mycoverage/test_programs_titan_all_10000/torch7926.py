import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
vec1 = torch.tensor([[10], [20]], dtype=torch.float32)
vec2 = torch.tensor([[100], [200]], dtype=torch.float32)
result = torch.Tensor.addr(input_tensor, vec1, vec2, beta=1, alpha=1)