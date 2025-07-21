'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Linear\ntorch.nn.Linear(in_features, out_features, bias=True, device=None, dtype=None)\n'
import torch
x = torch.randn(1, 3)
print(x)
linear = torch.nn.Linear(3, 1)
print(linear)
print(linear(x))