import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.randn(10, 10)
torch.use_deterministic_algorithms(True)
output_data = torch.randn(10, 10)