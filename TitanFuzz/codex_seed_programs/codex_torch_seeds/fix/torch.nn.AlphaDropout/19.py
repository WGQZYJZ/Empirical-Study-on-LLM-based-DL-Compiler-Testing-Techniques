'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AlphaDropout\ntorch.nn.AlphaDropout(p=0.5, inplace=False)\n'
import torch
import torch.nn as nn
input_data = torch.randn(2, 3)
print(input_data)
alpha_dropout = nn.AlphaDropout(p=0.5, inplace=False)
output_data = alpha_dropout(input_data)
print(output_data)