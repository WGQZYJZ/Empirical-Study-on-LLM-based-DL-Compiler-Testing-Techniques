'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Linear\ntorch.nn.Linear(in_features, out_features, bias=True, device=None, dtype=None)\n'
import torch
x = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
linear = torch.nn.Linear(2, 1)
print(linear)
y = linear(x)
print(y)
linear = torch.nn.Linear(2, 1, bias=False)
print(linear)
y = linear(x)
print(y)
linear = torch.nn.Linear(2, 1, bias=True)
print(linear)
y = linear(x)
print(y)
linear = torch.nn.Linear