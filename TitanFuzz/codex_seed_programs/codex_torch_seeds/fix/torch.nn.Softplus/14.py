'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softplus\ntorch.nn.Softplus(beta=1, threshold=20)\n'
import torch
import torch.nn as nn
x = torch.randn(3, requires_grad=True)
print(x)
softplus = nn.Softplus(beta=1, threshold=20)
y = softplus(x)
print(y)