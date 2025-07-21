"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.spectral_norm\ntorch.nn.utils.spectral_norm(module, name='weight', n_power_iterations=1, eps=1e-12, dim=None)\n"
import torch
import torch.nn as nn
import torch
import torch.nn as nn
input = torch.randn(20, 20)
linear = nn.Linear(20, 20)
s = nn.utils.spectral_norm(linear)
output = s(input)
print(output)