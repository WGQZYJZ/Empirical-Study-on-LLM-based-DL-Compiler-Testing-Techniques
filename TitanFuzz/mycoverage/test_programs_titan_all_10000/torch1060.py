import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([2, 4, 8, 16], dtype=torch.float32)
output_data = torch.log2(input_data)