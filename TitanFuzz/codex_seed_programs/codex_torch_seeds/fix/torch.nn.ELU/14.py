'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ELU\ntorch.nn.ELU(alpha=1.0, inplace=False)\n'
import torch
import torch.nn as nn
input_data = torch.randn(2, 3)
elu = nn.ELU()
output_data = elu(input_data)
print(input_data)
print(output_data)
elu = nn.ELU(alpha=0.5)
output_data = elu(input_data)
print(input_data)
print(output_data)
elu = nn.ELU(alpha=0.5, inplace=True)
output_data = elu(input_data)
print(input_data)
print(output_data)