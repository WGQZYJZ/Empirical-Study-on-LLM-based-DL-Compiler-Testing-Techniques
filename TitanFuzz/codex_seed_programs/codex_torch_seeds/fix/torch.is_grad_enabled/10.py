'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_grad_enabled\ntorch.is_grad_enabled()\n'
import torch
x = torch.tensor(2.0, requires_grad=True)
y = (((((2 * (x ** 4)) + (x ** 3)) + (3 * (x ** 2))) + (5 * x)) + 1)
y.backward()
print(x.grad)