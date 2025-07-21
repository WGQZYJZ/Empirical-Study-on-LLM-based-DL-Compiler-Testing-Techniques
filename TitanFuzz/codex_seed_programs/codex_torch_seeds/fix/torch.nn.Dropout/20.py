'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Dropout\ntorch.nn.Dropout(p=0.5, inplace=False)\n'
import torch
input_data = torch.randn(20, 16)
print(input_data)
output_data = torch.nn.Dropout(p=0.5)(input_data)
print(output_data)