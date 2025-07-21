'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.relu\ntorch.nn.functional.relu(input, inplace=False)\n'
import torch
input_data = torch.randn(100, 100)
relu_output = torch.nn.functional.relu(input_data)
print('relu_output:', relu_output)