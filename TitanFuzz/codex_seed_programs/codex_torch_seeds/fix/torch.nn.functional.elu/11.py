'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.elu\ntorch.nn.functional.elu(input, alpha=1.0, inplace=False)\n'
import torch
import torch
input_data = torch.randn(1, 1, 3, 3)
print(input_data)
output_data = torch.nn.functional.elu(input_data)
print(output_data)