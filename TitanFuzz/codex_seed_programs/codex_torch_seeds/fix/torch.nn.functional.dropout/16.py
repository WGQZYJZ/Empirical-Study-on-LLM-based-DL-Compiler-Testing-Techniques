'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.dropout\ntorch.nn.functional.dropout(input, p=0.5, training=True, inplace=False)\n'
import torch
input_data = torch.randn(10, 1, 1, 3)
print(input_data)
output_data = torch.nn.functional.dropout(input_data, p=0.5, training=True, inplace=False)
print(output_data)