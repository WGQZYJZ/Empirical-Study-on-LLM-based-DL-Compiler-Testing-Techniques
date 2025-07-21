'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.leaky_relu\ntorch.nn.functional.leaky_relu(input, negative_slope=0.01, inplace=False)\n'
import torch
import torch.nn.functional as F
input_data = torch.randn(10, 5)
print(input_data)
output = F.leaky_relu(input_data, negative_slope=0.01, inplace=False)
print(output)