import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.Tensor([[4, 12, (- 16)], [12, 37, (- 43)], [(- 16), (- 43), 98]])
torch.cholesky(input_data)