import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([0.0, 0.2, 0.4, 0.6, 0.8, 1.0], dtype=torch.float32)
output_data = torch.special.erf(input_data)