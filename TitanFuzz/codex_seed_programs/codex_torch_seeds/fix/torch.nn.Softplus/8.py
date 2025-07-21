'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softplus\ntorch.nn.Softplus(beta=1, threshold=20)\n'
import torch
x = torch.randn(3, requires_grad=True)
print(x)
y = torch.nn.Softplus()(x)
print(y)
y.backward(torch.tensor([1.0, 1.0, 1.0]))
print(x.grad)