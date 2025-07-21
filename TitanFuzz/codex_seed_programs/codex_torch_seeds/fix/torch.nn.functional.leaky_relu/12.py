'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.leaky_relu\ntorch.nn.functional.leaky_relu(input, negative_slope=0.01, inplace=False)\n'
import torch
import torch
input_data = torch.randn(2, 2)
torch.nn.functional.leaky_relu(input_data, negative_slope=0.01, inplace=False)
print(input_data)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.elu\ntorch.nn.functional.elu(input, alpha=1.0, inplace=False)\n'
import torch
import torch
input_data = torch.randn(2, 2)
torch.nn.functional.elu(input_data, alpha=1.0, inplace=False)