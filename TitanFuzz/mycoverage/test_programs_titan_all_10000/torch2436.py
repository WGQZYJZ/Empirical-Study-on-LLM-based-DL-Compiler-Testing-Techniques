import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[3.0, 3.3], [4.0, 5.9], [6.0, 7.5], [8.1, 9.2], [10.1, 11.3], [12.9, 13.2]], dtype=torch.float32)
output_data = torch.full(size=[6, 2], fill_value=1.0)