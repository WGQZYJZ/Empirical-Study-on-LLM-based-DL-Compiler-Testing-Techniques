'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.trace\ntorch.trace(input)\n'
import torch
input_data = torch.randn(2, 3)
print(input_data)
trace = torch.trace(input_data)
print(trace)