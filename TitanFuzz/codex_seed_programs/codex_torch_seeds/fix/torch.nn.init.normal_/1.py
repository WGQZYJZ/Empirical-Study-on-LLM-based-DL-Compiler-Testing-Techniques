'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.normal_\ntorch.nn.init.normal_(tensor, mean=0.0, std=1.0)\n'
import torch
import torch
x = torch.empty(2, 3)
print(x)
torch.nn.init.normal_(x)
print(x)
torch.nn.init.normal_(x, mean=1.0)
print(x)
torch.nn.init.normal_(x, std=2.0)
print(x)
torch.nn.init.normal_(x, mean=1.0, std=2.0)
print(x)
torch.nn.init.normal_(x, mean=2.0, std=2.0)
print(x)