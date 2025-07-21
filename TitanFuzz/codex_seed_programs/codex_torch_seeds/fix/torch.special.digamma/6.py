'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.digamma\ntorch.special.digamma(input, *, out=None)\n'
import torch
import numpy as np
input_tensor = torch.tensor([0.1, 0.2, 0.3, 0.4, 0.5])
output_tensor = torch.special.digamma(input_tensor)
print(output_tensor)