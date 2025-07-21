'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.relu\ntorch.nn.functional.relu(input, inplace=False)\n'
import torch
import torch
input_data = torch.randn(1, 1, 3, 3)
print(input_data)
output_data = torch.nn.functional.relu(input_data)
print(output_data)