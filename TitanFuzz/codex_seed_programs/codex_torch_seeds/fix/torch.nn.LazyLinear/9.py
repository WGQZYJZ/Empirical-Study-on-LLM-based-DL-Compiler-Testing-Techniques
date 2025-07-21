'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LazyLinear\ntorch.nn.LazyLinear(out_features, bias=True, device=None, dtype=None)\n'
import torch
x = torch.tensor([[1.0, 1], [1, 2], [3, 4]], dtype=torch.float)
print(x)
linear = torch.nn.LazyLinear(2, 2)
print(linear)
y = linear(x)
print(y)