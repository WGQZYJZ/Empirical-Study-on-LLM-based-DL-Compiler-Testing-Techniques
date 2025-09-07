import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
output = torch.Tensor.item(input_tensor)