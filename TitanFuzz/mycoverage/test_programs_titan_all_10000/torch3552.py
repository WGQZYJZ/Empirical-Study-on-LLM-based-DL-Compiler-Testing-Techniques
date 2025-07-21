import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([1.1, 2.2, 3.3, 4.4], dtype=torch.float32)
output_data = torch.round(input_data)