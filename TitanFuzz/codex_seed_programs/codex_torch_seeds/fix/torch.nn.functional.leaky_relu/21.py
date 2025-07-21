'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.leaky_relu\ntorch.nn.functional.leaky_relu(input, negative_slope=0.01, inplace=False)\n'
import torch
import torch.nn.functional as F
import torch
x = torch.rand(3, 5)
out = F.leaky_relu(x, negative_slope=0.01, inplace=False)
print(out)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.elu\ntorch.nn.functional.elu(input, alpha=1.0, inplace=False)\n'
import torch
import torch.nn.functional as F
import torch
x = torch.rand(3, 5)