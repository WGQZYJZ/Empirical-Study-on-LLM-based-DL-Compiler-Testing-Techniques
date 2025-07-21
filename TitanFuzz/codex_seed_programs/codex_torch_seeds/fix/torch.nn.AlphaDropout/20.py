'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AlphaDropout\ntorch.nn.AlphaDropout(p=0.5, inplace=False)\n'
import torch
x = torch.randn(2, 2)
print(x)
dropout = torch.nn.AlphaDropout(p=0.5, inplace=False)
y = dropout(x)
print(y)