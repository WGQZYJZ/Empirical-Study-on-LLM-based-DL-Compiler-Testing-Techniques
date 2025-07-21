'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cos\ntorch.cos(input, *, out=None)\n'
import torch
input_data = torch.randn(1, 3, requires_grad=True)
print('Input data: ', input_data)
cos_output = torch.cos(input_data)
print('Cosine output: ', cos_output)