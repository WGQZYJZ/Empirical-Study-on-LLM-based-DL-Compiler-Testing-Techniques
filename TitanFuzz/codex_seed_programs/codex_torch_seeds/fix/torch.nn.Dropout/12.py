'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Dropout\ntorch.nn.Dropout(p=0.5, inplace=False)\n'
import torch
x = torch.randn(100, 200)
dropout = torch.nn.Dropout(p=0.5)
y = dropout(x)
print(x.size())
print(y.size())