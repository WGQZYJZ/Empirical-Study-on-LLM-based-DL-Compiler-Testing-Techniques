import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 1, 3, 3)
output = torch.nn.functional.local_response_norm(input_data, 1)