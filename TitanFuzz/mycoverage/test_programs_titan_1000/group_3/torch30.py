import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([(- 1.0), 0.0, 1.0, 2.0, 3.0, 4.0])
output_data = torch.clip(input_data, min=1.0, max=3.0)