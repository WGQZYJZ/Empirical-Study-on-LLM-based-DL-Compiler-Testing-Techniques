'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AlphaDropout\ntorch.nn.AlphaDropout(p=0.5, inplace=False)\n'
import torch
import torch.nn as nn
input_data = torch.randn(1, 3)
dropout = nn.AlphaDropout(p=0.5)
output = dropout(input_data)
print(output)