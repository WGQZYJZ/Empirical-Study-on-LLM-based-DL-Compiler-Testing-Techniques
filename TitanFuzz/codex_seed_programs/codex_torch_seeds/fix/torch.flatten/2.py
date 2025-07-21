'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.flatten\ntorch.flatten(input, start_dim=0, end_dim=-1)\n'
import torch
input_data = torch.randn(2, 3, 4)
print(input_data)
print(torch.flatten(input_data))
print(torch.flatten(input_data, start_dim=1))
print(torch.flatten(input_data, end_dim=1))