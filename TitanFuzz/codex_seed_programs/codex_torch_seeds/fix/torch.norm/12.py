"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.norm\ntorch.norm(input, p='fro', dim=None, keepdim=False, out=None, dtype=None)\n"
import torch
input_data = torch.randn(2, 3)
print('input_data:', input_data)
norm = torch.norm(input_data, p='fro')
print('norm:', norm)