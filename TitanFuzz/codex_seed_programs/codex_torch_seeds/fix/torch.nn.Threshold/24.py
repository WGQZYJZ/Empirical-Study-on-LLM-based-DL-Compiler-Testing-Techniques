'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Threshold\ntorch.nn.Threshold(threshold, value, inplace=False)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
input = torch.randn(1, 3, 3)
threshold = nn.Threshold(0.5, 0)
output = threshold(input)
print(input)
print(output)