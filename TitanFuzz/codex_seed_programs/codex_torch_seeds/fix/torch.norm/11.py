"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.norm\ntorch.norm(input, p='fro', dim=None, keepdim=False, out=None, dtype=None)\n"
import torch
input_data = torch.randn(2, 3)
print('input_data: ', input_data)
norm_1 = torch.norm(input_data, p=1)
print('norm_1: ', norm_1)
norm_2 = torch.norm(input_data, p=2)
print('norm_2: ', norm_2)
norm_3 = torch.norm(input_data, p=3)
print('norm_3: ', norm_3)
norm_inf = torch.norm(input_data, p=float('inf'))
print('norm_inf: ', norm_inf)