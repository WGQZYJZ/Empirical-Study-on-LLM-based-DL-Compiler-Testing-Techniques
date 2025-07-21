'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.parameter.UninitializedParameter\ntorch.nn.parameter.UninitializedParameter(requires_grad=True, device=None, dtype=None)\n'
import torch
from torch.autograd import Variable
input_data = Variable(torch.ones(5, 5))
weight = torch.nn.parameter.UninitializedParameter(requires_grad=True, device=None, dtype=None)
print(weight)