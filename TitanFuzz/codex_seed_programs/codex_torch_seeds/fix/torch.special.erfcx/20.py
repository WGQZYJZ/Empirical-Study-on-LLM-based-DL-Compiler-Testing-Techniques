'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.erfcx\ntorch.special.erfcx(input, *, out=None)\n'
import torch
import numpy as np
input_data = torch.randn(10, dtype=torch.float64)
output = torch.special.erfcx(input_data)
print(input_data)
print(output)