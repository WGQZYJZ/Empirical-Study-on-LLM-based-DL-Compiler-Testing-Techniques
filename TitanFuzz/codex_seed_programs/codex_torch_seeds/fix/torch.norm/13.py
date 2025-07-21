"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.norm\ntorch.norm(input, p='fro', dim=None, keepdim=False, out=None, dtype=None)\n"
import torch
input_data = torch.rand(2, 3, 4, 5)
output_data_default_p = torch.norm(input_data)
output_data_p1 = torch.norm(input_data, p=1)
output_data_p_inf = torch.norm(input_data, p=float('inf'))
output_data_dim0 = torch.norm(input_data, dim=0)