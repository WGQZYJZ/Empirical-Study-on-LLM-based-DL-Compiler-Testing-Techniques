"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.weight_norm\ntorch.nn.utils.weight_norm(module, name='weight', dim=0)\n"
import torch
from torch.nn import Linear
import torch
input_data = torch.randn(20, 5)
linear = Linear(5, 10)
linear = torch.nn.utils.weight_norm(linear)
output = linear(input_data)
print(output)