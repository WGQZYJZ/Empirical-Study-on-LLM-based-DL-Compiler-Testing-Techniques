'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Dropout\ntorch.nn.Dropout(p=0.5, inplace=False)\n'
import torch
input = torch.randn(10, 10)
dropout = torch.nn.Dropout(p=0.5, inplace=False)
output = dropout(input)
print(output)