'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Linear\ntorch.nn.Linear(in_features, out_features, bias=True, device=None, dtype=None)\n'
import torch
from torch.autograd import Variable
input_data = Variable(torch.randn(1, 10))
linear_layer = torch.nn.Linear(10, 1)
output = linear_layer(input_data)
print(output)