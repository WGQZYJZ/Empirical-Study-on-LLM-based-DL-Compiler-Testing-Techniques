'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.det\ntorch.det(input)\n'
import torch
input_data = torch.randn(2, 3, 3)
print(input_data)
print(torch.det(input_data))