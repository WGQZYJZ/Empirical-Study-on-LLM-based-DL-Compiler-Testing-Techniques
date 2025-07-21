'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softplus\ntorch.nn.Softplus(beta=1, threshold=20)\n'
import torch
x = torch.randn(10)
print(x)
y = torch.nn.Softplus(beta=1, threshold=20)
print(y(x))