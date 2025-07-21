'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.leaky_relu\ntorch.nn.functional.leaky_relu(input, negative_slope=0.01, inplace=False)\n'
import torch
import torch.nn.functional as F
x = torch.randn(1, 1, 3, 3)
print(x)
y = F.leaky_relu(x, negative_slope=0.01, inplace=False)
print(y)
'\nTask 4: Call the API torch.nn.functional.elu\ntorch.nn.functional.elu(input, alpha=1.0, inplace=False)\n'
y = F.elu(x, alpha=1.0, inplace=False)
print(y)
'\nTask 5: Call the API torch.nn.functional.relu\ntorch.nn.functional.relu(input, inplace=False)\n'
y = F.relu(x, inplace=False)
print(y)
'\nTask 6: Call the API torch.nn.functional.prelu\ntorch.nn.functional.prelu(input, weight)\n'
weight = torch.tensor([0.5])