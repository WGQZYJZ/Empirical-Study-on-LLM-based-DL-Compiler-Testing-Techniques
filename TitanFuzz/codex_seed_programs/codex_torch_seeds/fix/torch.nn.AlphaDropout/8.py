'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AlphaDropout\ntorch.nn.AlphaDropout(p=0.5, inplace=False)\n'
import torch
x = torch.randn(1, 1, 3, 3)
print(x)
torch.nn.AlphaDropout(p=0.5, inplace=False)
print(x)