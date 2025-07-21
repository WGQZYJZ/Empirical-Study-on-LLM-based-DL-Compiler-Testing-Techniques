'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.trapz\ntorch.trapz(y, *, dx=1, dim=-1)\n'
import torch
import numpy as np
x = torch.linspace(0, (2 * np.pi), steps=100, dtype=torch.float64)
y = torch.sin(x)
integral = torch.trapz(y, x=x)
print(integral)
integral = torch.trapz(y, x=x)
print(integral)