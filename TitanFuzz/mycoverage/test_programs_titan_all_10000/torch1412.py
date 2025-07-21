import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randint(0, 10, (4, 4), dtype=torch.float32)
result = torch.Tensor.equal(input_tensor, input_tensor)
input_tensor = torch.randint(0, 10, (4, 4), dtype=torch.float32)
result = torch.Tensor.equal(input_tensor, input_tensor)