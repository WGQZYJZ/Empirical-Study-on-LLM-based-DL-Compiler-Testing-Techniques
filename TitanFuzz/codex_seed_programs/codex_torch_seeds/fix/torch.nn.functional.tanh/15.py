'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.tanh\ntorch.nn.functional.tanh(input)\n'
import torch
data = torch.randn(5)
print(data)
print(torch.nn.functional.tanh(data))