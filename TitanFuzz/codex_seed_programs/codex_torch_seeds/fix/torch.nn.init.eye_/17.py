'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.eye_\ntorch.nn.init.eye_(tensor)\n'
import torch
import torch
x = torch.empty(3, 3)
y = torch.empty(3, 3)
torch.nn.init.eye_(x)
torch.nn.init.eye_(y)
print(x)
print(y)