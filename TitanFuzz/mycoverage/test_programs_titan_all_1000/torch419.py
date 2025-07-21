import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
result = torch.is_floating_point(input_tensor)