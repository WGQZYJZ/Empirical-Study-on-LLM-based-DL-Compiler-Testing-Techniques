'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Dropout2d\ntorch.nn.Dropout2d(p=0.5, inplace=False)\n'
import torch
x = torch.ones(1, 1, 2, 2)
print(x)
torch.nn.Dropout2d(p=0.5, inplace=False)(x)
print(x)