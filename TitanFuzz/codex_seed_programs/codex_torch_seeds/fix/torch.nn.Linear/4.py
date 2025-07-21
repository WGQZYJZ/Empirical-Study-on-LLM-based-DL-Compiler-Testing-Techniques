'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Linear\ntorch.nn.Linear(in_features, out_features, bias=True, device=None, dtype=None)\n'
import torch
X = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
linear = torch.nn.Linear(3, 1)
print(linear)
y = linear(X)
print(y)