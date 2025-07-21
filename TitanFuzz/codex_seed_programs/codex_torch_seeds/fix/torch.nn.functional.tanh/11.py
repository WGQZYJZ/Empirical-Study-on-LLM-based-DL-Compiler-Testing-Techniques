'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.tanh\ntorch.nn.functional.tanh(input)\n'
import torch
data = torch.randn(4, 4)
print(data)
print('\n')
print(torch.nn.functional.tanh(data))