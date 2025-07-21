'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.trace\ntorch.trace(input)\n'
import torch
x = torch.randn(3, 3)
print('x:', x)
trace = torch.trace(x)
print('trace:', trace)