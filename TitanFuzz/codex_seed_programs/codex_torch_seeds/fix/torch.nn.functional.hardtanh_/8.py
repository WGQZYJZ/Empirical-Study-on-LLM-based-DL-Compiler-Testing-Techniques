'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.hardtanh_\ntorch.nn.functional.hardtanh_(input, min_val=-1., max_val=1.)\n'
import torch
input_data = torch.randn(1, 1, 2, 2)
print(input_data)
output_data = torch.nn.functional.hardtanh_(input_data)
print(output_data)
output_data = torch.nn.functional.hardtanh_(input_data, min_val=0.5, max_val=1.5)
print(output_data)