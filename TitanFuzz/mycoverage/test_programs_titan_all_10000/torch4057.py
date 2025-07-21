import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(3, 3)
torch.use_deterministic_algorithms(mode=True)
output_data = torch.rand(3, 3)