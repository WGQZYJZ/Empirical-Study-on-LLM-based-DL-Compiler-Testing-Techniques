'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.softplus\ntorch.nn.functional.softplus(input, beta=1, threshold=20)\n'
import torch
x = torch.randn(3, requires_grad=True)
print(x)
y = torch.nn.functional.softplus(x)
print(y)
y.backward(torch.tensor([1, 1, 1]))
print(x.grad)