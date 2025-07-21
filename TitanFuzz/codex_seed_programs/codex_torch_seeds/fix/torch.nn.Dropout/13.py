'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Dropout\ntorch.nn.Dropout(p=0.5, inplace=False)\n'
import torch
x = torch.ones(5, 5)
print(x)
dropout = torch.nn.Dropout(p=0.5, inplace=False)
print(dropout)
y = dropout(x)
print(y)