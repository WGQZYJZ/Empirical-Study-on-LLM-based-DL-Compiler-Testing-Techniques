'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.uniform_\ntorch.nn.init.uniform_(tensor, a=0.0, b=1.0)\n'
import torch
input_data = torch.randn(2, 3)
print(input_data)
torch.nn.init.uniform_(input_data, a=0.0, b=1.0)
print(input_data)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.normal_\ntorch.nn.init.normal_(tensor, mean=0.0, std=1.0)\n'
import torch
input_data = torch.randn(2, 3)
print(input_data)
torch.nn.init.normal_(input_data, mean=0.0, std=1.0)
print(input_data)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.xavier_normal_\ntorch.nn.init.xavier_normal_(tensor, gain=1.0)\n'
import torch
input_data = torch.rand