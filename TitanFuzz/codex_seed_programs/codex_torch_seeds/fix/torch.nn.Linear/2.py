'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Linear\ntorch.nn.Linear(in_features, out_features, bias=True, device=None, dtype=None)\n'
import torch
x = torch.tensor([[1.0, 2.0], [3.0, 4.0]], requires_grad=True)
linear = torch.nn.Linear(2, 1)
y = linear(x)
print(y)
y.backward(torch.ones_like(y))
print(x.grad)