import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(3, 3)
result = torch.triu_indices(row=3, col=3, offset=0, dtype=torch.long, device='cpu', layout=torch.strided)