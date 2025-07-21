'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.zeros_\ntorch.nn.init.zeros_(tensor)\n'
import torch
input_data = torch.randn(5, 3)
torch.nn.init.zeros_(input_data)
print(input_data)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.ones_\ntorch.nn.init.ones_(tensor)\n'
import torch
input_data = torch.randn(5, 3)
torch.nn.init.ones_(input_data)
print(input_data)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.normal_\ntorch.nn.init.normal_(tensor, mean=0, std=1)\n'
import torch
input_data = torch.randn(5, 3)
torch.nn.init.normal_(input_data)
print(input_data)