'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.are_deterministic_algorithms_enabled\ntorch.are_deterministic_algorithms_enabled()\n'
import torch
x = torch.randn(2, 3, requires_grad=True)
y = torch.randn(2, 3, requires_grad=True)
z = torch.randn(2, 3, requires_grad=True)
a = (x + y)
b = (a + z)
c = torch.sum(b)
c.backward()
print(x.grad)
print(y.grad)
print(z.grad)
print(torch.are_deterministic_algorithms_enabled())