'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Hardtanh\ntorch.nn.Hardtanh(min_val=-1.0, max_val=1.0, inplace=False, min_value=None, max_value=None)\n'
import torch
import torch
input_data = torch.randn(1, 3, 5, 5)
print(input_data)
output_data = torch.nn.Hardtanh(min_val=(- 2.0), max_val=2.0)(input_data)
print(output_data)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReLU\ntorch.nn.ReLU(inplace=False)\n'
import torch
import torch
input_data = torch.randn(1, 3, 5, 5)
print(input_data)
output_data = torch.nn.ReLU()(input_data)
print(output_data)