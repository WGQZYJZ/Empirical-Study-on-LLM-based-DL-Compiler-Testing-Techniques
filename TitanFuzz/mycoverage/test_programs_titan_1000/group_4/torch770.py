import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randint(0, 2, (4, 4), dtype=torch.uint8)
other_data = torch.randint(0, 2, (4, 4), dtype=torch.uint8)
output_data = torch.bitwise_and(input_data, other_data)