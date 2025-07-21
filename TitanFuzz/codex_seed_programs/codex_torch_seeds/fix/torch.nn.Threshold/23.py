'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Threshold\ntorch.nn.Threshold(threshold, value, inplace=False)\n'
import torch
input = torch.randn(1, 3)
print('Input data: ', input)
threshold = torch.nn.Threshold(0.5, 0.0)
output = threshold(input)
print('Output data: ', output)