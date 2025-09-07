import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([1, 2, 3], dtype=torch.float32)
output_data = torch.log(input_data)