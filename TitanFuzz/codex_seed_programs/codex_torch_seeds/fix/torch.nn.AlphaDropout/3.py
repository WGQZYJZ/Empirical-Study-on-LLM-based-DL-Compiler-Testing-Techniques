'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AlphaDropout\ntorch.nn.AlphaDropout(p=0.5, inplace=False)\n'
import torch
input = torch.randn(20, 16)
print(input)
dropout = torch.nn.AlphaDropout(p=0.5, inplace=False)
output = dropout(input)
print(output)