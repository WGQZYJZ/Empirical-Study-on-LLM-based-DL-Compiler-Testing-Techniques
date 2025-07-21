'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.uniform_\ntorch.nn.init.uniform_(tensor, a=0.0, b=1.0)\n'
import torch
import torch
x = torch.empty(3, 3)
torch.nn.init.uniform_(x, a=0.0, b=1.0)
print(x)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.normal_\ntorch.nn.init.normal_(tensor, mean=0.0, std=1.0)\n'
import torch
import torch
x = torch.empty(3, 3)
torch.nn.init.normal_(x, mean=0.0, std=1.0)
print(x)