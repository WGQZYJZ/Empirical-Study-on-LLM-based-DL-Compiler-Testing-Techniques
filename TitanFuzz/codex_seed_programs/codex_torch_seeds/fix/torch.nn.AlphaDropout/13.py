'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AlphaDropout\ntorch.nn.AlphaDropout(p=0.5, inplace=False)\n'
import torch
import torch.nn as nn
input = torch.Tensor(3, 5)
input.data.normal_(0, 1)
dropout = nn.AlphaDropout(p=0.5, inplace=False)
output = dropout(input)
print(output)