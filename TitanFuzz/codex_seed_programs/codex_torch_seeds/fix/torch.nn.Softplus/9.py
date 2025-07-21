'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softplus\ntorch.nn.Softplus(beta=1, threshold=20)\n'
import torch
import torch.nn as nn
input_data = torch.randn(1, 2)
print('input_data: ', input_data)
softplus = nn.Softplus(beta=1, threshold=20)
output = softplus(input_data)
print('output: ', output)