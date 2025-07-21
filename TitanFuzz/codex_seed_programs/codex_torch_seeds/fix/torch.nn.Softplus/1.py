'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softplus\ntorch.nn.Softplus(beta=1, threshold=20)\n'
import torch
import torch.nn as nn
x = torch.randn(1, 3)
softplus_layer = nn.Softplus()
y = softplus_layer(x)
print(y)