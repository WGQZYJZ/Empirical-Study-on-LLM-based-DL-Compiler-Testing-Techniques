"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.spectral_norm\ntorch.nn.utils.spectral_norm(module, name='weight', n_power_iterations=1, eps=1e-12, dim=None)\n"
import torch
import torch.nn as nn
import torch.nn.functional as F
input_data = torch.randn(20, 20)
m = nn.Linear(20, 30)
m = nn.utils.spectral_norm(m)
print(m(input_data).size())