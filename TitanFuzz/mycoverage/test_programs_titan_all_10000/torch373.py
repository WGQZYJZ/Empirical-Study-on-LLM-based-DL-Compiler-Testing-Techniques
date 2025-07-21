import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, 2, 3], [3, 2, 1], [1, 1, 1]], dtype=torch.float32)
pinverse_tensor = torch.Tensor.pinverse(input_tensor)