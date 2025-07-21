'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Threshold\ntorch.nn.Threshold(threshold, value, inplace=False)\n'
import torch
x = torch.randn(3, 3)
print(x)
threshold = torch.nn.Threshold(0.5, 0.5)
y = threshold(x)
print(y)