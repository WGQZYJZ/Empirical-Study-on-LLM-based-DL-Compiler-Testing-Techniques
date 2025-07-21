'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Threshold\ntorch.nn.Threshold(threshold, value, inplace=False)\n'
import torch
import torch
input = torch.randn(4, 4)
print('Input:', input)
output = torch.nn.Threshold(0.5, 0.5)(input)
print('Output:', output)