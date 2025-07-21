'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReLU\ntorch.nn.ReLU(inplace=False)\n'
import torch
input_data = torch.randn(1, 10)
print(input_data)
relu = torch.nn.ReLU()
output = relu(input_data)
print(output)