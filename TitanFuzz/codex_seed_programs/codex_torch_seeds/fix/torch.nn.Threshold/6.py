'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Threshold\ntorch.nn.Threshold(threshold, value, inplace=False)\n'
import torch
import torch
x = torch.rand(2, 3)
print('x:', x)
threshold = 0.5
value = (- 1)
y = torch.nn.Threshold(threshold, value)(x)
print('y:', y)
threshold = 0.5
value = (- 1)
y = torch.nn.Threshold(threshold, value, inplace=True)(x)
print('y:', y)
print('x:', x)