'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Tanh\ntorch.nn.Tanh()\n'
import torch
x = torch.randn(1, 3)
print('Input: ', x)
tanh = torch.nn.Tanh()
print('Output: ', tanh(x))