'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.t\ntorch.t(input)\n'
import torch
input_data = torch.randn(2, 3)
print(input_data)
transpose_data = torch.t(input_data)
print(transpose_data)